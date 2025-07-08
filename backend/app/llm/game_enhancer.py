"""
LLM-powered game idea enhancer
Uses OpenAI API to suggest improvements to game ideas
"""

import os
import json
from typing import List, Dict, Any
from openai import OpenAI
from pydantic import BaseModel

class GameEnhancement(BaseModel):
    category: str
    suggestions: List[str]
    description: str

class GameEnhancer:
    def __init__(self):
        """Initialize the game enhancer with OpenAI client"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        self.client = OpenAI(api_key=api_key)
        
        # Define enhancement categories
        self.categories = {
            "mechanics": "Gameplay mechanics and player abilities",
            "levels": "Level design and environment ideas", 
            "story": "Narrative elements and character development"
        }
    
    async def enhance_idea(self, game_idea: str, genre: str = "general") -> List[GameEnhancement]:
        """
        Take a game idea and suggest enhancements across different categories
        
        Args:
            game_idea: The original game description
            genre: Game genre (platformer, rpg, puzzle, etc.)
            
        Returns:
            List of GameEnhancement objects with suggestions
        """
        
        # Create the enhancement prompt
        prompt = self._create_enhancement_prompt(game_idea, genre)
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert game designer who helps enhance game ideas with creative suggestions."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0.8,  # Creative but focused
                max_tokens=1000
            )
            
            # Parse the response
            content = response.choices[0].message.content
            enhancements = self._parse_enhancements(content)
            
            return enhancements
            
        except Exception as e:
            # Fallback to basic suggestions if API fails
            print(f"API call failed: {e}")
            return self._generate_fallback_enhancements(game_idea, genre)
    
    def _create_enhancement_prompt(self, game_idea: str, genre: str) -> str:
        """Create a detailed prompt for the LLM"""
        
        return f"""
        I have a game idea: "{game_idea}"
        Genre: {genre}
        
        Please suggest enhancements in these categories:
        
        1. MECHANICS: Suggest 3-5 gameplay mechanics, abilities, or systems that would make this game more engaging
        2. LEVELS: Suggest 3-5 level design ideas, environments, or progression elements
        3. STORY: Suggest 3-5 narrative elements, character motivations, or world-building ideas
        
        Format your response as JSON:
        {{
            "mechanics": {{
                "suggestions": ["mechanic1", "mechanic2", "mechanic3"],
                "description": "Brief explanation of mechanics category"
            }},
            "levels": {{
                "suggestions": ["level1", "level2", "level3"],
                "description": "Brief explanation of levels category"
            }},
            "story": {{
                "suggestions": ["story1", "story2", "story3"],
                "description": "Brief explanation of story category"
            }}
        }}
        
        Make suggestions that are:
        - Specific and actionable
        - Appropriate for the genre
        - Creative but realistic for a prototype
        - Easy to implement in Unity
        """
    
    def _parse_enhancements(self, content: str) -> List[GameEnhancement]:
        """Parse the LLM response into structured enhancements"""
        
        try:
            # Try to extract JSON from the response
            # Sometimes the LLM wraps JSON in markdown or adds extra text
            if "```json" in content:
                json_start = content.find("```json") + 7
                json_end = content.find("```", json_start)
                json_str = content[json_start:json_end].strip()
            elif "{" in content and "}" in content:
                json_start = content.find("{")
                json_end = content.rfind("}") + 1
                json_str = content[json_start:json_end]
            else:
                raise ValueError("No JSON found in response")
            
            data = json.loads(json_str)
            
            enhancements = []
            for category, details in data.items():
                if category in self.categories:
                    enhancement = GameEnhancement(
                        category=category,
                        suggestions=details.get("suggestions", []),
                        description=details.get("description", self.categories[category])
                    )
                    enhancements.append(enhancement)
            
            return enhancements
            
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Failed to parse LLM response: {e}")
            # Return fallback suggestions
            return self._generate_fallback_enhancements("", "general")
    
    def _generate_fallback_enhancements(self, game_idea: str, genre: str) -> List[GameEnhancement]:
        """Generate basic fallback suggestions when LLM fails"""
        
        fallback_suggestions = {
            "mechanics": {
                "suggestions": [
                    "Double jump ability",
                    "Collectible items",
                    "Health system",
                    "Power-ups",
                    "Basic movement controls"
                ],
                "description": "Core gameplay mechanics for player interaction"
            },
            "levels": {
                "suggestions": [
                    "Multiple levels with increasing difficulty",
                    "Secret areas to discover",
                    "Checkpoint system",
                    "Different environments",
                    "Boss battle areas"
                ],
                "description": "Level design and progression elements"
            },
            "story": {
                "suggestions": [
                    "Main character with a goal",
                    "Antagonist or obstacle to overcome",
                    "World-building elements",
                    "Character motivation",
                    "Simple narrative arc"
                ],
                "description": "Narrative and character development ideas"
            }
        }
        
        enhancements = []
        for category, details in fallback_suggestions.items():
            enhancement = GameEnhancement(
                category=category,
                suggestions=details["suggestions"],
                description=details["description"]
            )
            enhancements.append(enhancement)
        
        return enhancements
    
    def get_available_categories(self) -> Dict[str, str]:
        """Get available enhancement categories"""
        return self.categories.copy() 
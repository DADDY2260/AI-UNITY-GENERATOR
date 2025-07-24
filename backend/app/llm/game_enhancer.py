"""
LLM-powered game idea enhancer with RAG integration
Uses OpenAI API with RAG pipeline to suggest improvements to game ideas
"""

import os
import json
from typing import List, Dict, Any
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from pydantic import BaseModel
from ..rag.rag_pipeline import RAGPipeline

class GameEnhancement(BaseModel):
    category: str
    suggestions: List[str]
    description: str

class GameEnhancer:
    def __init__(self):
        """Initialize the game enhancer with Hugging Face Mistral-7B and RAG pipeline"""
        # Load Mistral-7B model and tokenizer
        model_name = "mistralai/Mistral-7B-Instruct-v0.2"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto", use_auth_token=True)
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer, device=0 if torch.cuda.is_available() else -1)

        # Initialize RAG pipeline
        self.rag_pipeline = RAGPipeline()
        # Define enhancement categories
        self.categories = {
            "mechanics": "Gameplay mechanics and player abilities",
            "levels": "Level design and environment ideas",
            "story": "Narrative elements and character development",
            "audio": "Audio and music suggestions",
            "visual": "Visual effects and art style suggestions",
            "uiux": "UI/UX improvements and interface ideas",
            "cutscenes": "Cutscene and dialogue ideas"
        }
    
    async def enhance_idea(self, game_idea: str, genre: str = "general") -> List[GameEnhancement]:
        """
        Take a game idea and suggest enhancements across different categories
        """
        # Create the enhancement prompt
        original_prompt = self._create_enhancement_prompt(game_idea, genre)
        # Enhance prompt with RAG
        enhanced_prompt = self.rag_pipeline.enhance_prompt_with_rag(
            original_prompt, game_idea, genre
        )
        try:
            # Use Hugging Face pipeline for text generation
            prompt = (
                "You are an expert game designer who helps enhance game ideas with creative suggestions. "
                "Use the provided knowledge base information to give more specific, actionable, and Unity-appropriate suggestions.\n" + enhanced_prompt
            )
            response = self.generator(prompt, max_new_tokens=1000, temperature=0.8, do_sample=True)
            content = response[0]["generated_text"]
            enhancements = self._parse_enhancements(content)
            return enhancements
        except Exception as e:
            print(f"LLM call failed: {e}")
            return self._generate_fallback_enhancements(game_idea, genre)
    
    def _create_enhancement_prompt(self, game_idea: str, genre: str) -> str:
        """Create a detailed prompt for the LLM"""
        
        is_3d = any(g in genre.lower() for g in ["3d", "3d platformer", "3d adventure", "3d shooter", "3d puzzle"])
        dimension_note = "This is a 3D game. Please make all suggestions and mechanics appropriate for 3D gameplay (e.g., 3D movement, camera, physics, etc.)." if is_3d else ""
        
        return f"""
        I have a game idea: \"{game_idea}\"
        Genre: {genre}
        {dimension_note}
        
        Please suggest enhancements in these categories:
        
        1. MECHANICS: Suggest 3-5 gameplay mechanics, abilities, or systems that would make this game more engaging
        2. LEVELS: Suggest 3-5 level design ideas, environments, or progression elements
        3. STORY: Suggest 3-5 narrative elements, character motivations, or world-building ideas
        4. AUDIO: Suggest 2-3 audio or music ideas that fit the game
        5. VISUAL: Suggest 2-3 visual effects, art styles, or animations
        6. UIUX: Suggest 2-3 UI/UX improvements or interface ideas
        7. CUTSCENES: Suggest 2-3 cutscene or dialogue moments
        
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
            }},
            "audio": {{
                "suggestions": ["audio1", "audio2"],
                "description": "Brief explanation of audio category"
            }},
            "visual": {{
                "suggestions": ["visual1", "visual2"],
                "description": "Brief explanation of visual category"
            }},
            "uiux": {{
                "suggestions": ["uiux1", "uiux2"],
                "description": "Brief explanation of UI/UX category"
            }},
            "cutscenes": {{
                "suggestions": ["cutscene1", "cutscene2"],
                "description": "Brief explanation of cutscenes category"
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
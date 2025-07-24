"""
RAG Pipeline for AI Unity Game Generator
Retrieves relevant game design knowledge and Unity information to enhance LLM responses
"""

import os
import json
from typing import List, Dict, Any, Optional
from pathlib import Path
import hashlib
from openai import OpenAI
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAGPipeline:
    def __init__(self, knowledge_base_path: str = "knowledge_base"):
        """
        Initialize RAG pipeline with knowledge base
        
        Args:
            knowledge_base_path: Path to knowledge base directory
        """
        self.knowledge_base_path = Path(knowledge_base_path)
        self.knowledge_base_path.mkdir(exist_ok=True)
        
        # Initialize OpenAI client (optional for basic functionality)
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            self.client = None
            print("⚠️  Warning: OPENAI_API_KEY not set. Some features may be limited.")
        
        # Initialize vectorizer for similarity search
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        
        # Load or create knowledge base
        self.knowledge_base = self._load_knowledge_base()
        self._create_embeddings()
    
    def _load_knowledge_base(self) -> Dict[str, Any]:
        """Load knowledge base from files or create default one"""
        kb_file = self.knowledge_base_path / "knowledge_base.json"
        
        if kb_file.exists():
            with open(kb_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Create default knowledge base
            default_kb = self._create_default_knowledge_base()
            self._save_knowledge_base(default_kb)
            return default_kb
    
    def _create_default_knowledge_base(self) -> Dict[str, Any]:
        """Create a default knowledge base with game design and Unity information"""
        return {
            "game_design": {
                "platformer_mechanics": [
                    "Double jump allows players to reach higher platforms",
                    "Wall jumping enables vertical movement and exploration",
                    "Dash ability provides quick horizontal movement",
                    "Collectibles encourage exploration and replayability",
                    "Checkpoint system reduces frustration and maintains progress"
                ],
                "rpg_elements": [
                    "Character progression through experience points",
                    "Inventory system for managing items and equipment",
                    "Quest system for structured gameplay objectives",
                    "Dialogue system for storytelling and character interaction",
                    "Combat mechanics with different attack types"
                ],
                "shooter_mechanics": [
                    "Aim and shoot mechanics with mouse/keyboard or controller",
                    "Weapon switching for different combat situations",
                    "Health and armor systems for player survival",
                    "Enemy AI with different behavior patterns",
                    "Cover system for tactical gameplay"
                ],
                "puzzle_elements": [
                    "Logic puzzles requiring problem-solving skills",
                    "Physics-based puzzles using game world interactions",
                    "Pattern recognition challenges",
                    "Environmental puzzles using level elements",
                    "Time-based puzzles adding urgency"
                ]
            },
            "unity_specific": {
                "player_controller": [
                    "Use Input.GetAxis for smooth movement",
                    "Apply forces to Rigidbody for physics-based movement",
                    "Use Transform.Translate for direct position changes",
                    "Implement ground checking with raycasts",
                    "Use Animator for smooth animations"
                ],
                "game_management": [
                    "Use GameManager singleton for global game state",
                    "Implement scene management with SceneManager",
                    "Use PlayerPrefs for saving game data",
                    "Create event system for loose coupling",
                    "Use coroutines for time-based actions"
                ],
                "ui_systems": [
                    "Use Canvas for UI layout and scaling",
                    "Implement UI Manager for centralized UI control",
                    "Use Text components for displaying information",
                    "Create button interactions with OnClick events",
                    "Use UI animations for smooth transitions"
                ],
                "audio_systems": [
                    "Use AudioSource component for sound playback",
                    "Implement AudioManager for centralized audio control",
                    "Use AudioMixer for volume and effects management",
                    "Create sound pools for performance optimization",
                    "Use 3D audio for spatial sound effects"
                ]
            },
            "best_practices": {
                "code_organization": [
                    "Separate concerns with different script components",
                    "Use inheritance for similar game objects",
                    "Implement interfaces for flexible design",
                    "Use ScriptableObjects for data-driven design",
                    "Follow Unity naming conventions"
                ],
                "performance": [
                    "Use object pooling for frequently created objects",
                    "Optimize with LOD (Level of Detail) systems",
                    "Use culling for off-screen objects",
                    "Minimize garbage collection with proper memory management",
                    "Use async operations for non-blocking code"
                ],
                "user_experience": [
                    "Provide clear visual feedback for player actions",
                    "Implement smooth camera movement and transitions",
                    "Use consistent input mapping across the game",
                    "Provide accessibility options for different players",
                    "Create intuitive UI with clear navigation"
                ]
            }
        }
    
    def _save_knowledge_base(self, kb: Dict[str, Any]):
        """Save knowledge base to file"""
        kb_file = self.knowledge_base_path / "knowledge_base.json"
        with open(kb_file, 'w', encoding='utf-8') as f:
            json.dump(kb, f, indent=2, ensure_ascii=False)
    
    def _create_embeddings(self):
        """Create embeddings for knowledge base entries"""
        # Flatten knowledge base into searchable documents
        self.documents = []
        self.document_metadata = []
        
        for category, subcategories in self.knowledge_base.items():
            for subcategory, items in subcategories.items():
                for item in items:
                    self.documents.append(item)
                    self.document_metadata.append({
                        "category": category,
                        "subcategory": subcategory,
                        "content": item
                    })
        
        # Create TF-IDF vectors for similarity search
        if self.documents:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
    
    def retrieve_relevant_info(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve relevant information from knowledge base
        
        Args:
            query: Search query
            top_k: Number of top results to return
            
        Returns:
            List of relevant documents with metadata
        """
        if not self.documents:
            return []
        
        # Transform query using same vectorizer
        query_vector = self.vectorizer.transform([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        
        # Get top k most similar documents
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # Minimum similarity threshold
                results.append({
                    **self.document_metadata[idx],
                    "similarity_score": float(similarities[idx])
                })
        
        return results
    
    def enhance_prompt_with_rag(self, original_prompt: str, game_idea: str, genre: str = "general") -> str:
        """
        Enhance the original prompt with retrieved relevant information
        
        Args:
            original_prompt: The original prompt
            game_idea: The game idea description
            genre: Game genre
            
        Returns:
            Enhanced prompt with retrieved context
        """
        # Create search queries based on game idea and genre
        search_queries = [
            game_idea,
            genre,
            f"{genre} mechanics",
            f"{genre} game design",
            "Unity best practices"
        ]
        
        # Retrieve relevant information
        relevant_info = []
        for query in search_queries:
            results = self.retrieve_relevant_info(query, top_k=3)
            relevant_info.extend(results)
        
        # Remove duplicates and sort by relevance
        unique_info = {}
        for info in relevant_info:
            key = info["content"]
            if key not in unique_info or info["similarity_score"] > unique_info[key]["similarity_score"]:
                unique_info[key] = info
        
        # Sort by similarity score
        sorted_info = sorted(unique_info.values(), key=lambda x: x["similarity_score"], reverse=True)
        
        # Create context from retrieved information
        context_parts = []
        for info in sorted_info[:10]:  # Top 10 most relevant
            context_parts.append(f"- {info['content']} (Category: {info['category']}/{info['subcategory']})")
        
        if context_parts:
            context = "\n".join(context_parts)
            enhanced_prompt = f"""
{original_prompt}

RELEVANT GAME DESIGN AND UNITY KNOWLEDGE:
{context}

Please use this knowledge to provide more specific, actionable, and Unity-appropriate suggestions.
"""
        else:
            enhanced_prompt = original_prompt
        
        return enhanced_prompt
    
    def add_to_knowledge_base(self, category: str, subcategory: str, content: List[str]):
        """
        Add new information to the knowledge base
        
        Args:
            category: Main category (e.g., "game_design", "unity_specific")
            subcategory: Subcategory (e.g., "platformer_mechanics", "player_controller")
            content: List of content items to add
        """
        if category not in self.knowledge_base:
            self.knowledge_base[category] = {}
        
        if subcategory not in self.knowledge_base[category]:
            self.knowledge_base[category][subcategory] = []
        
        self.knowledge_base[category][subcategory].extend(content)
        
        # Save updated knowledge base
        self._save_knowledge_base(self.knowledge_base)
        
        # Recreate embeddings
        self._create_embeddings()
    
    def get_knowledge_base_stats(self) -> Dict[str, Any]:
        """Get statistics about the knowledge base"""
        total_items = 0
        category_stats = {}
        
        for category, subcategories in self.knowledge_base.items():
            category_count = 0
            for subcategory, items in subcategories.items():
                category_count += len(items)
                total_items += len(items)
            category_stats[category] = category_count
        
        return {
            "total_items": total_items,
            "categories": category_stats,
            "document_count": len(self.documents) if hasattr(self, 'documents') else 0
        } 
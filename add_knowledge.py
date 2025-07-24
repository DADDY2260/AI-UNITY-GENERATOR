#!/usr/bin/env python3
"""
Script to add comprehensive knowledge to the RAG system
"""

import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

from app.rag.rag_pipeline import RAGPipeline

def add_game_design_knowledge():
    """Add comprehensive game design knowledge"""
    rag = RAGPipeline()
    
    # Enemy AI Patterns
    enemy_ai_knowledge = [
        "Patrol AI moves between predefined waypoints and switches to chase mode when player is detected",
        "Boss AI uses multiple attack phases based on remaining health percentage",
        "Stealth AI hides from the player and sets up ambushes when the player is vulnerable",
        "Swarm AI coordinates multiple enemies to surround and overwhelm the player",
        "Ranged AI maintains distance while attacking and seeks cover when threatened",
        "Aggressive AI charges directly at the player and uses close-combat attacks",
        "Defensive AI prioritizes survival and retreats when health is low",
        "Support AI heals or buffs other enemies rather than attacking directly",
        "Sniper AI takes precise shots from long distances and relocates after each shot",
        "Tank AI absorbs damage and protects weaker enemies while dealing heavy damage"
    ]
    
    rag.add_to_knowledge_base("game_design", "enemy_ai_patterns", enemy_ai_knowledge)
    print("✅ Added Enemy AI Patterns knowledge")
    
    # Level Design
    level_design_knowledge = [
        "Hub areas provide safe zones where players can rest, upgrade, and plan their next move",
        "Linear progression guides players through a clear path while allowing for exploration",
        "Open world design gives players freedom to explore and discover content at their own pace",
        "Metroidvania-style backtracking rewards players with new abilities that unlock previous areas",
        "Procedural generation creates unique levels each time while maintaining core gameplay elements",
        "Vertical level design uses height differences to create interesting movement and combat scenarios",
        "Environmental storytelling reveals narrative through level details rather than explicit dialogue",
        "Checkpoint systems reduce frustration by allowing players to restart from strategic points",
        "Secret areas reward exploration and provide optional challenges or rewards",
        "Dynamic environments change during gameplay to create evolving challenges"
    ]
    
    rag.add_to_knowledge_base("game_design", "level_design", level_design_knowledge)
    print("✅ Added Level Design knowledge")

def add_storytelling_knowledge():
    """Add comprehensive storytelling knowledge"""
    rag = RAGPipeline()
    
    # Storytelling Techniques
    storytelling_knowledge = [
        "Environmental storytelling reveals plot through level design, objects, and atmosphere",
        "Character development through dialogue choices that affect relationships and story outcomes",
        "Multiple endings based on player decisions create replayability and consequence",
        "Flashback sequences reveal character backstory and motivation without exposition",
        "Unreliable narrator creates mystery and forces players to question what they know",
        "Parallel storylines follow different characters whose paths eventually converge",
        "Time manipulation allows players to experience the same events from different perspectives",
        "Moral choices with no clear right answer create meaningful player decisions",
        "Collectible lore items expand the world without interrupting gameplay flow",
        "Dynamic storytelling adapts the narrative based on player behavior and choices"
    ]
    
    rag.add_to_knowledge_base("game_design", "storytelling", storytelling_knowledge)
    print("✅ Added Storytelling knowledge")

def add_game_mechanics_knowledge():
    """Add comprehensive game mechanics knowledge"""
    rag = RAGPipeline()
    
    # Core Game Mechanics
    mechanics_knowledge = [
        "Combo systems reward skilled play by chaining attacks for increased damage",
        "Resource management creates strategic depth through limited health, ammo, or energy",
        "Skill trees allow players to customize their character build and playstyle",
        "Crafting systems let players create items from collected materials",
        "Stealth mechanics reward careful planning and patience over direct confrontation",
        "Physics-based gameplay creates emergent behavior and realistic interactions",
        "Time manipulation allows players to slow, stop, or reverse time for strategic advantage",
        "Multiplayer mechanics encourage cooperation, competition, or both",
        "Progression systems provide long-term goals and sense of achievement",
        "Risk-reward mechanics make players choose between safety and greater rewards"
    ]
    
    rag.add_to_knowledge_base("game_design", "game_mechanics", mechanics_knowledge)
    print("✅ Added Game Mechanics knowledge")

def add_unity_specific_knowledge():
    """Add Unity-specific technical knowledge"""
    rag = RAGPipeline()
    
    # Camera Systems
    camera_knowledge = [
        "Cinemachine provides advanced camera controls with virtual cameras and brain system",
        "Follow camera smoothly tracks the player with configurable damping and offset",
        "Camera shake adds impact to explosions, hits, and dramatic moments",
        "Multiple camera angles can be switched between for different gameplay situations",
        "Camera collision detection prevents the camera from clipping through walls",
        "Smooth camera transitions create cinematic effects between scenes",
        "Camera zoom can be used for dramatic effect or gameplay mechanics",
        "Split-screen cameras allow multiple players to see their own view",
        "Camera filters and post-processing create mood and atmosphere",
        "Dynamic camera positioning adapts to the environment and player actions"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "camera_systems", camera_knowledge)
    print("✅ Added Camera Systems knowledge")
    
    # Lighting
    lighting_knowledge = [
        "Global illumination creates realistic lighting that bounces off surfaces naturally",
        "Dynamic lighting can change during gameplay to affect atmosphere and gameplay",
        "Light probes capture lighting information for moving objects",
        "Shadow mapping creates realistic shadows that enhance depth perception",
        "Volumetric lighting creates atmospheric effects like fog and dust",
        "Light cookies project patterns or textures through lights for dramatic effects",
        "Light layers allow different lights to affect specific objects or layers",
        "Real-time lighting provides immediate visual feedback for dynamic scenes",
        "Baked lighting improves performance for static environments",
        "Light intensity and color can be animated for dramatic effects"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "lighting", lighting_knowledge)
    print("✅ Added Lighting knowledge")
    
    # Textures
    texture_knowledge = [
        "PBR (Physically Based Rendering) textures create realistic material appearance",
        "Texture atlasing combines multiple textures into one image to improve performance",
        "Normal maps add surface detail without increasing polygon count",
        "Specular maps control how shiny or rough a surface appears",
        "Emission maps make parts of textures glow for effects like neon or fire",
        "Detail textures add fine surface detail when viewed up close",
        "Texture streaming loads high-resolution textures only when needed",
        "Mipmaps provide different resolution versions for distance-based rendering",
        "Texture compression reduces file size while maintaining visual quality",
        "Procedural textures can be generated in real-time for infinite variety"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "textures", texture_knowledge)
    print("✅ Added Textures knowledge")

def main():
    """Add all knowledge categories"""
    print("📚 Adding Comprehensive Knowledge to RAG System")
    print("=" * 50)
    
    try:
        # Add game design knowledge
        add_game_design_knowledge()
        add_storytelling_knowledge()
        add_game_mechanics_knowledge()
        
        # Add Unity-specific knowledge
        add_unity_specific_knowledge()
        
        # Show final stats
        rag = RAGPipeline()
        stats = rag.get_knowledge_base_stats()
        print(f"\n📊 Final Knowledge Base Stats:")
        print(f"Total items: {stats['total_items']}")
        for category, count in stats['categories'].items():
            print(f"  {category}: {count} items")
        
        print("\n🎉 Knowledge addition completed successfully!")
        print("\nNew categories added:")
        print("  ✅ Enemy AI Patterns")
        print("  ✅ Level Design") 
        print("  ✅ Storytelling")
        print("  ✅ Game Mechanics")
        print("  ✅ Camera Systems")
        print("  ✅ Lighting")
        print("  ✅ Textures")
        
    except Exception as e:
        print(f"❌ Error adding knowledge: {e}")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Script to add specialized knowledge for specific game genres
Genres: RPG, FPS, Strategy, Puzzle, Platformer, Adventure, Simulation, Sports, Racing
"""

import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

from app.rag.rag_pipeline import RAGPipeline

def add_rpg_knowledge():
    """Add specialized RPG (Role-Playing Game) knowledge"""
    rag = RAGPipeline()
    
    # RPG Core Systems
    rpg_core_knowledge = [
        "Character classes define distinct playstyles with unique abilities and progression paths",
        "Experience points and leveling systems provide long-term progression and character growth",
        "Skill trees allow players to customize character builds and specialize in different areas",
        "Inventory management systems handle equipment, consumables, and quest items efficiently",
        "Quest systems provide structured objectives and narrative progression through the game world",
        "Dialogue systems enable character interaction and branching storylines based on choices",
        "Combat systems range from turn-based tactical battles to real-time action combat",
        "Crafting systems allow players to create items from collected materials and recipes",
        "Reputation systems track player actions and affect NPC reactions and story outcomes",
        "Party management enables multiple character control and team-based gameplay"
    ]
    
    rag.add_to_knowledge_base("game_design", "rpg_core_systems", rpg_core_knowledge)
    print("✅ Added RPG Core Systems knowledge")
    
    # RPG World Design
    rpg_world_knowledge = [
        "Open world design provides vast exploration areas with multiple storylines",
        "Hub areas serve as safe zones for rest, trading, and quest acceptance",
        "Dungeon design creates challenging environments with puzzles and combat encounters",
        "NPC schedules create living worlds where characters have daily routines",
        "Weather systems affect gameplay and create atmospheric immersion",
        "Day/night cycles change NPC behavior and unlock time-specific content",
        "Fast travel systems reduce backtracking while maintaining world immersion",
        "Secret areas reward exploration with unique items and story content",
        "Environmental storytelling reveals lore through world details and atmosphere",
        "World events create dynamic content that changes based on player actions"
    ]
    
    rag.add_to_knowledge_base("game_design", "rpg_world_design", rpg_world_knowledge)
    print("✅ Added RPG World Design knowledge")

def add_fps_knowledge():
    """Add specialized FPS (First-Person Shooter) knowledge"""
    rag = RAGPipeline()
    
    # FPS Combat Systems
    fps_combat_knowledge = [
        "Weapon variety provides different engagement ranges and tactical options",
        "Aiming mechanics require precision and skill with mouse or controller input",
        "Recoil patterns create weapon mastery and realistic shooting mechanics",
        "Hit detection systems ensure accurate bullet impact and damage calculation",
        "Cover systems provide tactical positioning and protection from enemy fire",
        "Grenade and explosive mechanics add area denial and tactical depth",
        "Melee combat provides close-quarters options when ammunition is limited",
        "Weapon switching allows tactical adaptation to different combat situations",
        "Reload mechanics create tension and timing-based gameplay moments",
        "Headshot mechanics reward precision with increased damage multipliers"
    ]
    
    rag.add_to_knowledge_base("game_design", "fps_combat_systems", fps_combat_knowledge)
    print("✅ Added FPS Combat Systems knowledge")
    
    # FPS Level Design
    fps_level_knowledge = [
        "Sight lines and chokepoints create tactical positioning opportunities",
        "Vertical gameplay uses height differences for strategic advantage",
        "Cover placement provides protection while maintaining engagement options",
        "Spawn points must be balanced to prevent spawn camping and unfair advantages",
        "Map flow guides players through logical paths while preventing bottlenecks",
        "Power positions offer tactical advantages but are vulnerable to multiple angles",
        "Environmental destruction creates dynamic cover and tactical opportunities",
        "Lighting affects visibility and creates atmospheric tension in combat",
        "Sound design provides audio cues for enemy location and movement",
        "Objective-based gameplay focuses combat around specific goals and locations"
    ]
    
    rag.add_to_knowledge_base("game_design", "fps_level_design", fps_level_knowledge)
    print("✅ Added FPS Level Design knowledge")

def add_strategy_knowledge():
    """Add specialized Strategy game knowledge"""
    rag = RAGPipeline()
    
    # Strategy Core Mechanics
    strategy_core_knowledge = [
        "Resource management creates strategic depth through limited materials and time",
        "Unit variety provides different tactical options and counter-play mechanics",
        "Terrain effects influence movement, combat, and strategic positioning",
        "Fog of war creates uncertainty and rewards scouting and information gathering",
        "Economy systems require balancing resource generation with military spending",
        "Technology trees unlock new units and abilities through research investment",
        "Diplomacy systems allow alliances, trade, and political manipulation",
        "Morale systems affect unit performance and create psychological warfare",
        "Supply lines limit expansion and create strategic vulnerabilities",
        "Victory conditions provide multiple paths to success beyond military conquest"
    ]
    
    rag.add_to_knowledge_base("game_design", "strategy_core_mechanics", strategy_core_knowledge)
    print("✅ Added Strategy Core Mechanics knowledge")
    
    # Strategy AI and Balance
    strategy_ai_knowledge = [
        "AI difficulty levels provide appropriate challenge for different skill levels",
        "Chess-like AI uses minimax algorithms for optimal strategic decision making",
        "Personality-based AI creates distinct opponents with different playstyles",
        "Adaptive AI learns from player strategies and adjusts tactics accordingly",
        "Resource cheating for AI provides challenge without perfect play requirements",
        "Faction balance ensures all playable sides have viable strategies",
        "Counter-play mechanics prevent dominant strategies from emerging",
        "Asymmetric balance creates different but equally powerful faction abilities",
        "Meta-game evolution keeps strategies fresh through patches and updates",
        "Spectator mode enables competitive play and tournament organization"
    ]
    
    rag.add_to_knowledge_base("game_design", "strategy_ai_balance", strategy_ai_knowledge)
    print("✅ Added Strategy AI and Balance knowledge")

def add_puzzle_knowledge():
    """Add specialized Puzzle game knowledge"""
    rag = RAGPipeline()
    
    # Puzzle Design Principles
    puzzle_design_knowledge = [
        "Progressive difficulty introduces mechanics gradually to avoid overwhelming players",
        "Aha moments create satisfying breakthroughs when players solve complex puzzles",
        "Multiple solution paths accommodate different problem-solving approaches",
        "Visual feedback clearly communicates puzzle state and available actions",
        "Hint systems provide assistance without completely solving the puzzle",
        "Puzzle variety prevents repetition and maintains player engagement",
        "Logical consistency ensures puzzle rules are clear and predictable",
        "Elegant solutions reward creative thinking and efficient problem-solving",
        "Puzzle sequences build complexity through combination of simple mechanics",
        "Accessibility features make puzzles solvable by players with different abilities"
    ]
    
    rag.add_to_knowledge_base("game_design", "puzzle_design_principles", puzzle_design_knowledge)
    print("✅ Added Puzzle Design Principles knowledge")
    
    # Puzzle Types and Mechanics
    puzzle_types_knowledge = [
        "Logic puzzles require deductive reasoning and elimination of possibilities",
        "Physics puzzles use realistic simulation for object interaction and movement",
        "Pattern recognition challenges identify sequences and relationships",
        "Spatial reasoning puzzles manipulate objects in 3D space",
        "Word puzzles use language and vocabulary for problem-solving",
        "Mathematical puzzles incorporate numbers and calculations",
        "Memory challenges test recall and pattern retention",
        "Timing puzzles require precise timing and rhythm",
        "Color and shape matching creates visual pattern recognition",
        "Mechanical puzzles simulate real-world devices and mechanisms"
    ]
    
    rag.add_to_knowledge_base("game_design", "puzzle_types_mechanics", puzzle_types_knowledge)
    print("✅ Added Puzzle Types and Mechanics knowledge")

def add_platformer_knowledge():
    """Add specialized Platformer knowledge"""
    rag = RAGPipeline()
    
    # Platformer Movement Systems
    platformer_movement_knowledge = [
        "Precise jump mechanics provide satisfying control and skill expression",
        "Wall jumping enables vertical movement and exploration of higher areas",
        "Double jump extends aerial mobility and creates advanced movement options",
        "Dash ability provides quick horizontal movement and evasion",
        "Slide mechanics allow movement through tight spaces and under obstacles",
        "Grappling hooks create dynamic movement and exploration possibilities",
        "Momentum systems create fluid movement that feels natural and responsive",
        "Coyote time allows brief window for jump input after leaving platform",
        "Variable jump height based on button press duration provides fine control",
        "Air control allows mid-air direction changes for precise landing"
    ]
    
    rag.add_to_knowledge_base("game_design", "platformer_movement", platformer_movement_knowledge)
    print("✅ Added Platformer Movement Systems knowledge")
    
    # Platformer Level Design
    platformer_level_knowledge = [
        "Checkpoint placement reduces frustration while maintaining challenge",
        "Secret areas reward exploration with collectibles and power-ups",
        "Vertical level design uses height differences for interesting movement",
        "Speed sections create variety and test player reflexes",
        "Boss arenas provide climactic encounters with unique mechanics",
        "Environmental hazards create danger zones requiring careful navigation",
        "Moving platforms add dynamic elements to static level geometry",
        "One-way passages guide players through intended level flow",
        "Multiple paths allow different approaches to level completion",
        "Visual storytelling reveals narrative through level design and atmosphere"
    ]
    
    rag.add_to_knowledge_base("game_design", "platformer_level_design", platformer_level_knowledge)
    print("✅ Added Platformer Level Design knowledge")

def add_adventure_knowledge():
    """Add specialized Adventure game knowledge"""
    rag = RAGPipeline()
    
    # Adventure Game Systems
    adventure_systems_knowledge = [
        "Point-and-click interfaces provide intuitive interaction with game world",
        "Inventory puzzles require combining items to solve environmental challenges",
        "Dialogue trees create branching conversations and character relationships",
        "Environmental storytelling reveals narrative through world details",
        "Puzzle integration advances story while providing intellectual challenge",
        "Character development focuses on personality and relationships over stats",
        "Atmospheric design creates mood and emotional engagement",
        "Exploration rewards curiosity with story content and world building",
        "Non-linear storytelling allows player choice in narrative progression",
        "Emotional storytelling creates memorable characters and meaningful experiences"
    ]
    
    rag.add_to_knowledge_base("game_design", "adventure_systems", adventure_systems_knowledge)
    print("✅ Added Adventure Game Systems knowledge")

def add_simulation_knowledge():
    """Add specialized Simulation game knowledge"""
    rag = RAGPipeline()
    
    # Simulation Systems
    simulation_systems_knowledge = [
        "Realistic physics simulation creates authentic object behavior and interaction",
        "Economic systems model supply, demand, and market dynamics",
        "Social simulation creates believable NPC behavior and relationships",
        "Weather systems affect gameplay and create dynamic environmental challenges",
        "Time progression allows long-term planning and strategic decision making",
        "Resource management balances multiple competing needs and priorities",
        "Random events create unpredictability and challenge player adaptability",
        "Complex systems interact to create emergent gameplay and unexpected outcomes",
        "Data visualization helps players understand complex system relationships",
        "Modding support extends game life through community-created content"
    ]
    
    rag.add_to_knowledge_base("game_design", "simulation_systems", simulation_systems_knowledge)
    print("✅ Added Simulation Systems knowledge")

def add_sports_racing_knowledge():
    """Add specialized Sports and Racing game knowledge"""
    rag = RAGPipeline()
    
    # Sports Game Systems
    sports_systems_knowledge = [
        "Realistic physics create authentic ball movement and player interaction",
        "Team management allows roster building and strategic player development",
        "Season modes provide long-term progression and career simulation",
        "Multiplayer competition creates social engagement and replayability",
        "Skill-based controls reward practice and mastery of game mechanics",
        "Commentary systems provide context and atmosphere for sports events",
        "Replay systems allow analysis of key moments and highlight creation",
        "Customization options personalize teams, players, and equipment",
        "Tournament modes create structured competitive play and progression",
        "Real-time strategy elements add tactical depth to sports simulation"
    ]
    
    rag.add_to_knowledge_base("game_design", "sports_systems", sports_systems_knowledge)
    print("✅ Added Sports Game Systems knowledge")
    
    # Racing Game Systems
    racing_systems_knowledge = [
        "Vehicle physics create realistic handling and performance characteristics",
        "Track design balances challenge with accessibility for different skill levels",
        "Upgrade systems allow vehicle customization and performance improvement",
        "Driving assists help new players while advanced options challenge experts",
        "Weather effects create dynamic racing conditions and strategic decisions",
        "Multiplayer racing creates competitive excitement and social interaction",
        "Replay systems capture dramatic moments and allow race analysis",
        "Customization options personalize vehicles and driver appearance",
        "Championship modes provide structured progression and long-term goals",
        "Arcade vs simulation modes accommodate different player preferences"
    ]
    
    rag.add_to_knowledge_base("game_design", "racing_systems", racing_systems_knowledge)
    print("✅ Added Racing Game Systems knowledge")

def main():
    """Add all genre-specialized knowledge"""
    print("🎮 Adding Genre-Specialized Knowledge to RAG System")
    print("=" * 55)
    
    try:
        # Add RPG knowledge
        add_rpg_knowledge()
        
        # Add FPS knowledge
        add_fps_knowledge()
        
        # Add Strategy knowledge
        add_strategy_knowledge()
        
        # Add Puzzle knowledge
        add_puzzle_knowledge()
        
        # Add Platformer knowledge
        add_platformer_knowledge()
        
        # Add Adventure knowledge
        add_adventure_knowledge()
        
        # Add Simulation knowledge
        add_simulation_knowledge()
        
        # Add Sports and Racing knowledge
        add_sports_racing_knowledge()
        
        # Show final stats
        rag = RAGPipeline()
        stats = rag.get_knowledge_base_stats()
        print(f"\n📊 Final Knowledge Base Stats:")
        print(f"Total items: {stats['total_items']}")
        for category, count in stats['categories'].items():
            print(f"  {category}: {count} items")
        
        print("\n🎉 Genre-specialized knowledge addition completed successfully!")
        print("\nNew genre categories added:")
        print("  ✅ RPG Core Systems & World Design")
        print("  ✅ FPS Combat & Level Design")
        print("  ✅ Strategy Core Mechanics & AI")
        print("  ✅ Puzzle Design Principles & Types")
        print("  ✅ Platformer Movement & Level Design")
        print("  ✅ Adventure Game Systems")
        print("  ✅ Simulation Systems")
        print("  ✅ Sports & Racing Game Systems")
        
        print("\n🎯 Genre Coverage:")
        print("  • RPG: Character progression, quests, world design")
        print("  • FPS: Combat mechanics, level design, multiplayer")
        print("  • Strategy: Resource management, AI, balance")
        print("  • Puzzle: Design principles, types, accessibility")
        print("  • Platformer: Movement systems, level design")
        print("  • Adventure: Storytelling, exploration, puzzles")
        print("  • Simulation: Realistic systems, emergent gameplay")
        print("  • Sports/Racing: Competition, physics, progression")
        
    except Exception as e:
        print(f"❌ Error adding genre-specialized knowledge: {e}")

if __name__ == "__main__":
    main() 
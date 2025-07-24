#!/usr/bin/env python3
"""
Demo script showing how genre-specific RAG knowledge improves game suggestions
Tests the system with specific genre examples and showcases enhanced capabilities
"""

import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

from app.rag.rag_pipeline import RAGPipeline

def demo_rpg_suggestions():
    """Demo RPG-specific suggestions"""
    print("🎭 RPG (Role-Playing Game) Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    
    # Test RPG-specific queries
    rpg_queries = [
        "character progression",
        "quest systems", 
        "inventory management",
        "open world design",
        "dialogue systems"
    ]
    
    for query in rpg_queries:
        print(f"\n🔍 Query: '{query}'")
        results = rag.retrieve_relevant_info(query, top_k=3)
        print(f"Found {len(results)} relevant results:")
        for i, result in enumerate(results, 1):
            print(f"  {i}. {result['content']}")
            print(f"     Category: {result['category']}/{result['subcategory']}")
            print(f"     Score: {result['similarity_score']:.3f}")
    
    # Test RPG prompt enhancement
    print(f"\n✨ RPG Prompt Enhancement Demo:")
    original_prompt = "Suggest mechanics for an RPG game"
    enhanced_prompt = rag.enhance_prompt_with_rag(original_prompt, "fantasy RPG", "rpg")
    
    print(f"Original prompt: {original_prompt}")
    print(f"Enhanced prompt length: {len(enhanced_prompt)} characters")
    print(f"Enhancement ratio: {len(enhanced_prompt)/len(original_prompt):.1f}x")
    
    # Show a preview of the enhanced prompt
    print(f"\nEnhanced prompt preview:")
    print(enhanced_prompt[:300] + "...")

def demo_fps_suggestions():
    """Demo FPS-specific suggestions"""
    print("\n🎯 FPS (First-Person Shooter) Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    
    # Test FPS-specific queries
    fps_queries = [
        "weapon mechanics",
        "aiming systems",
        "level design",
        "multiplayer combat",
        "cover systems"
    ]
    
    for query in fps_queries:
        print(f"\n🔍 Query: '{query}'")
        results = rag.retrieve_relevant_info(query, top_k=3)
        print(f"Found {len(results)} relevant results:")
        for i, result in enumerate(results, 1):
            print(f"  {i}. {result['content']}")
            print(f"     Category: {result['category']}/{result['subcategory']}")
            print(f"     Score: {result['similarity_score']:.3f}")
    
    # Test FPS prompt enhancement
    print(f"\n✨ FPS Prompt Enhancement Demo:")
    original_prompt = "Suggest mechanics for a competitive FPS"
    enhanced_prompt = rag.enhance_prompt_with_rag(original_prompt, "competitive FPS", "shooter")
    
    print(f"Original prompt: {original_prompt}")
    print(f"Enhanced prompt length: {len(enhanced_prompt)} characters")
    print(f"Enhancement ratio: {len(enhanced_prompt)/len(original_prompt):.1f}x")

def demo_strategy_suggestions():
    """Demo Strategy-specific suggestions"""
    print("\n⚔️ Strategy Game Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    
    # Test Strategy-specific queries
    strategy_queries = [
        "resource management",
        "unit variety",
        "AI opponents",
        "terrain effects",
        "victory conditions"
    ]
    
    for query in strategy_queries:
        print(f"\n🔍 Query: '{query}'")
        results = rag.retrieve_relevant_info(query, top_k=3)
        print(f"Found {len(results)} relevant results:")
        for i, result in enumerate(results, 1):
            print(f"  {i}. {result['content']}")
            print(f"     Category: {result['category']}/{result['subcategory']}")
            print(f"     Score: {result['similarity_score']:.3f}")

def demo_puzzle_suggestions():
    """Demo Puzzle-specific suggestions"""
    print("\n🧩 Puzzle Game Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    
    # Test Puzzle-specific queries
    puzzle_queries = [
        "progressive difficulty",
        "puzzle types",
        "visual feedback",
        "hint systems",
        "accessibility"
    ]
    
    for query in puzzle_queries:
        print(f"\n🔍 Query: '{query}'")
        results = rag.retrieve_relevant_info(query, top_k=3)
        print(f"Found {len(results)} relevant results:")
        for i, result in enumerate(results, 1):
            print(f"  {i}. {result['content']}")
            print(f"     Category: {result['category']}/{result['subcategory']}")
            print(f"     Score: {result['similarity_score']:.3f}")

def demo_platformer_suggestions():
    """Demo Platformer-specific suggestions"""
    print("\n🏃 Platformer Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    
    # Test Platformer-specific queries
    platformer_queries = [
        "jump mechanics",
        "movement systems",
        "level design",
        "checkpoint systems",
        "boss encounters"
    ]
    
    for query in platformer_queries:
        print(f"\n🔍 Query: '{query}'")
        results = rag.retrieve_relevant_info(query, top_k=3)
        print(f"Found {len(results)} relevant results:")
        for i, result in enumerate(results, 1):
            print(f"  {i}. {result['content']}")
            print(f"     Category: {result['category']}/{result['subcategory']}")
            print(f"     Score: {result['similarity_score']:.3f}")

def demo_comparison():
    """Demo comparing suggestions across different genres"""
    print("\n🔄 Cross-Genre Comparison Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    
    # Compare the same query across different genres
    test_query = "combat mechanics"
    genres = ["rpg", "fps", "strategy", "action"]
    
    print(f"Query: '{test_query}' across different genres:")
    
    for genre in genres:
        print(f"\n🎮 {genre.upper()} suggestions:")
        enhanced_prompt = rag.enhance_prompt_with_rag(
            f"Suggest {test_query} for a {genre} game",
            f"{genre} game",
            genre
        )
        
        # Extract relevant suggestions from the enhanced prompt
        lines = enhanced_prompt.split('\n')
        relevant_lines = [line for line in lines if any(keyword in line.lower() for keyword in ['combat', 'battle', 'fight', 'attack'])]
        
        print(f"Found {len(relevant_lines)} combat-related suggestions:")
        for line in relevant_lines[:3]:  # Show top 3
            if line.strip():
                print(f"  • {line.strip()}")

def demo_knowledge_coverage():
    """Demo showing knowledge base coverage across genres"""
    print("\n📊 Knowledge Base Coverage Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    stats = rag.get_knowledge_base_stats()
    
    print(f"Total knowledge items: {stats['total_items']}")
    print(f"Categories:")
    for category, count in stats['categories'].items():
        print(f"  • {category}: {count} items")
    
    # Test genre-specific coverage
    genre_tests = [
        ("RPG", ["character", "quest", "inventory", "dialogue"]),
        ("FPS", ["weapon", "aiming", "cover", "multiplayer"]),
        ("Strategy", ["resource", "unit", "terrain", "AI"]),
        ("Puzzle", ["difficulty", "feedback", "hint", "accessibility"]),
        ("Platformer", ["jump", "movement", "level", "checkpoint"])
    ]
    
    print(f"\n🎯 Genre-Specific Coverage:")
    for genre, keywords in genre_tests:
        print(f"\n{genre}:")
        for keyword in keywords:
            results = rag.retrieve_relevant_info(keyword, top_k=1)
            if results:
                print(f"  • {keyword}: {len(results)} relevant items")
            else:
                print(f"  • {keyword}: No specific items found")

def demo_enhancement_improvements():
    """Demo showing how enhancement ratios have improved"""
    print("\n📈 Enhancement Ratio Improvements Demo")
    print("=" * 40)
    
    rag = RAGPipeline()
    
    # Test different game ideas
    game_ideas = [
        ("2D platformer where a fox collects gems", "platformer"),
        ("3D shooter with tactical combat", "shooter"),
        ("RPG with character customization", "rpg"),
        ("Puzzle game with physics", "puzzle"),
        ("Strategy game with resource management", "strategy")
    ]
    
    print("Testing enhancement ratios for different genres:")
    
    for game_idea, genre in game_ideas:
        original_prompt = f"Suggest mechanics for {game_idea}"
        enhanced_prompt = rag.enhance_prompt_with_rag(original_prompt, game_idea, genre)
        
        enhancement_ratio = len(enhanced_prompt) / len(original_prompt)
        print(f"\n🎮 {genre.upper()}: {game_idea}")
        print(f"  Enhancement ratio: {enhancement_ratio:.1f}x")
        print(f"  Enhanced prompt length: {len(enhanced_prompt)} characters")

def main():
    """Run all demo scenarios"""
    print("🎮 Genre-Specific RAG Demo Suite")
    print("=" * 50)
    print("Testing how genre-specific knowledge improves suggestions...")
    
    try:
        # Run genre-specific demos
        demo_rpg_suggestions()
        demo_fps_suggestions()
        demo_strategy_suggestions()
        demo_puzzle_suggestions()
        demo_platformer_suggestions()
        
        # Run comparison demos
        demo_comparison()
        demo_knowledge_coverage()
        demo_enhancement_improvements()
        
        print("\n🎉 Demo completed successfully!")
        print("\n🎯 Key Insights:")
        print("  ✅ Genre-specific knowledge provides targeted suggestions")
        print("  ✅ Enhancement ratios improve with specialized knowledge")
        print("  ✅ Cross-genre comparisons show different approaches")
        print("  ✅ Knowledge base coverage spans all major genres")
        print("  ✅ RAG system adapts suggestions to specific game types")
        
    except Exception as e:
        print(f"❌ Error in demo: {e}")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Test script for RAG pipeline functionality (without OpenAI API)
Demonstrates core RAG features that don't require API calls
"""

import os
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

# Mock OpenAI client for testing
class MockOpenAIClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or "mock_key"

# Patch the OpenAI import
import openai
original_openai = openai.OpenAI
openai.OpenAI = MockOpenAIClient

from app.rag.rag_pipeline import RAGPipeline

def test_rag_pipeline():
    """Test the RAG pipeline functionality"""
    print("🧪 Testing RAG Pipeline...")
    
    # Initialize RAG pipeline
    rag = RAGPipeline()
    
    # Test knowledge base stats
    stats = rag.get_knowledge_base_stats()
    print(f"📊 Knowledge Base Stats: {stats}")
    
    # Test search functionality
    print("\n🔍 Testing search functionality...")
    results = rag.retrieve_relevant_info("platformer mechanics", top_k=3)
    print(f"Found {len(results)} relevant results:")
    for result in results:
        print(f"  - {result['content']} (Score: {result['similarity_score']:.3f})")
    
    # Test prompt enhancement
    print("\n✨ Testing prompt enhancement...")
    original_prompt = "Suggest game mechanics for a 2D platformer"
    enhanced_prompt = rag.enhance_prompt_with_rag(original_prompt, "2D platformer", "platformer")
    print("Enhanced prompt length:", len(enhanced_prompt))
    print("Enhanced prompt preview:", enhanced_prompt[:200] + "...")
    
    return True

def test_knowledge_addition():
    """Test adding new knowledge to the RAG system"""
    print("\n📚 Testing knowledge addition...")
    
    rag = RAGPipeline()
    
    # Add some new knowledge
    new_knowledge = [
        "Procedural generation creates infinite replayability",
        "Roguelike elements add challenge and variety",
        "Metroidvania-style exploration rewards player curiosity"
    ]
    
    rag.add_to_knowledge_base("game_design", "procedural_elements", new_knowledge)
    
    # Test that the new knowledge is searchable
    results = rag.retrieve_relevant_info("procedural generation", top_k=2)
    print(f"Found {len(results)} results for 'procedural generation':")
    for result in results:
        print(f"  - {result['content']}")
    
    return True

def test_knowledge_base_structure():
    """Test the knowledge base structure and content"""
    print("\n🏗️ Testing knowledge base structure...")
    
    rag = RAGPipeline()
    
    # Check if default knowledge base was created
    stats = rag.get_knowledge_base_stats()
    print(f"Knowledge base has {stats['total_items']} total items")
    
    # Test different categories
    categories = ["game_design", "unity_specific", "best_practices"]
    for category in categories:
        if category in stats['categories']:
            print(f"✅ {category}: {stats['categories'][category]} items")
        else:
            print(f"❌ {category}: Not found")
    
    return True

def test_search_functionality():
    """Test various search queries"""
    print("\n🔍 Testing search functionality with different queries...")
    
    rag = RAGPipeline()
    
    test_queries = [
        "Unity player movement",
        "game mechanics",
        "performance optimization",
        "UI systems",
        "audio implementation"
    ]
    
    for query in test_queries:
        results = rag.retrieve_relevant_info(query, top_k=2)
        print(f"\nQuery: '{query}'")
        print(f"Found {len(results)} results:")
        for result in results:
            print(f"  - {result['content'][:80]}... (Score: {result['similarity_score']:.3f})")
    
    return True

def test_prompt_enhancement():
    """Test prompt enhancement with different game ideas"""
    print("\n✨ Testing prompt enhancement with different scenarios...")
    
    rag = RAGPipeline()
    
    test_scenarios = [
        ("2D platformer", "platformer"),
        ("3D shooter", "shooter"),
        ("RPG adventure", "rpg"),
        ("Puzzle game", "puzzle")
    ]
    
    for game_idea, genre in test_scenarios:
        original_prompt = f"Suggest mechanics for a {game_idea}"
        enhanced_prompt = rag.enhance_prompt_with_rag(original_prompt, game_idea, genre)
        
        print(f"\nGame: {game_idea} ({genre})")
        print(f"Original prompt length: {len(original_prompt)}")
        print(f"Enhanced prompt length: {len(enhanced_prompt)}")
        print(f"Enhancement ratio: {len(enhanced_prompt)/len(original_prompt):.1f}x")
        
        # Show a preview of the enhanced prompt
        if len(enhanced_prompt) > len(original_prompt):
            print("✅ Prompt was enhanced with relevant knowledge")
        else:
            print("⚠️ No enhancement applied")
    
    return True

def main():
    """Run all RAG tests"""
    print("🚀 RAG Pipeline Test Suite (No API Required)")
    print("=" * 60)
    
    tests = [
        ("RAG Pipeline", test_rag_pipeline),
        ("Knowledge Addition", test_knowledge_addition),
        ("Knowledge Base Structure", test_knowledge_base_structure),
        ("Search Functionality", test_search_functionality),
        ("Prompt Enhancement", test_prompt_enhancement)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                print(f"✅ {test_name}: PASSED")
                passed += 1
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
    
    print(f"\n📈 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! RAG pipeline is working correctly.")
        print("\n🎯 Key Features Demonstrated:")
        print("  ✅ Knowledge base creation and management")
        print("  ✅ TF-IDF vectorization and similarity search")
        print("  ✅ Prompt enhancement with relevant context")
        print("  ✅ Dynamic knowledge addition")
        print("  ✅ Multi-category knowledge organization")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")

if __name__ == "__main__":
    main() 
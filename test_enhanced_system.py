#!/usr/bin/env python3
"""
Test script to demonstrate the enhanced RAG system with real game ideas
Shows how genre-specific knowledge improves suggestions
"""

import requests
import json
import time

def test_game_enhancement(game_idea, genre):
    """Test the enhanced game idea enhancement"""
    print(f"\n🎮 Testing: '{game_idea}' (Genre: {genre})")
    print("=" * 60)
    
    # Test the enhance-idea endpoint
    url = "http://localhost:8000/enhance-idea"
    data = {
        "description": game_idea,
        "genre": genre
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json()
            print("✅ Enhancement successful!")
            print(f"Original idea: {result['original_idea']}")
            print(f"Summary: {result['summary']}")
            
            # Show enhancements by category
            for enhancement in result['enhancements']:
                print(f"\n📋 {enhancement['category'].upper()}:")
                print(f"   Description: {enhancement['description']}")
                print("   Suggestions:")
                for i, suggestion in enumerate(enhancement['suggestions'], 1):
                    print(f"     {i}. {suggestion}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

def test_rag_search(query):
    """Test the RAG search functionality"""
    print(f"\n🔍 Testing RAG search: '{query}'")
    print("=" * 40)
    
    url = f"http://localhost:8000/rag/search?query={query}&top_k=5"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Found {len(result['results'])} relevant results:")
            
            for i, item in enumerate(result['results'], 1):
                print(f"  {i}. {item['content']}")
                print(f"     Category: {item['category']}/{item['subcategory']}")
                print(f"     Score: {item['similarity_score']:.3f}")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

def test_rag_stats():
    """Test the RAG statistics"""
    print("\n📊 RAG Knowledge Base Statistics")
    print("=" * 40)
    
    url = "http://localhost:8000/rag/stats"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            stats = result['stats']
            
            print(f"✅ Total items: {stats['total_items']}")
            print("Categories:")
            for category, count in stats['categories'].items():
                print(f"  • {category}: {count} items")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

def main():
    """Run comprehensive tests of the enhanced system"""
    print("🚀 Testing Enhanced RAG System")
    print("=" * 50)
    
    # Test RAG statistics first
    test_rag_stats()
    
    # Test different game ideas across genres
    test_cases = [
        ("2D platformer where a fox collects magical gems", "platformer"),
        ("3D shooter with tactical cover mechanics", "shooter"),
        ("RPG with character customization and skill trees", "rpg"),
        ("Puzzle game with physics-based challenges", "puzzle"),
        ("Strategy game with resource management", "strategy"),
        ("Adventure game with environmental storytelling", "adventure"),
        ("Racing game with realistic physics", "racing"),
        ("Sports game with multiplayer competition", "sports")
    ]
    
    for game_idea, genre in test_cases:
        test_game_enhancement(game_idea, genre)
        time.sleep(1)  # Small delay between requests
    
    # Test RAG search with specific queries
    search_queries = [
        "Unity player movement",
        "inventory systems",
        "weapon mechanics",
        "level design",
        "AI behavior",
        "performance optimization"
    ]
    
    for query in search_queries:
        test_rag_search(query)
        time.sleep(0.5)
    
    print("\n🎉 Enhanced system testing completed!")
    print("\n🎯 Key Features Demonstrated:")
    print("  ✅ Genre-specific game enhancement")
    print("  ✅ RAG-powered knowledge retrieval")
    print("  ✅ Comprehensive knowledge base")
    print("  ✅ Real-time suggestion generation")

if __name__ == "__main__":
    main() 
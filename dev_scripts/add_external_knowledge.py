#!/usr/bin/env python3
"""
Script to add knowledge from external sources
Sources: Unity Documentation, Game Design Blogs, Industry Best Practices
"""

import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

from app.rag.rag_pipeline import RAGPipeline

def add_unity_documentation_knowledge():
    """Add knowledge from Unity official documentation"""
    rag = RAGPipeline()
    
    # Unity Scripting API Best Practices
    unity_scripting_knowledge = [
        "Use ScriptableObjects for data-driven design to separate data from logic",
        "Implement interfaces for flexible component design and easy testing",
        "Use events and delegates for loose coupling between game systems",
        "Coroutines handle time-based operations without blocking the main thread",
        "Object pooling improves performance by reusing objects instead of instantiation",
        "Use [SerializeField] to expose private fields in the Inspector for debugging",
        "Implement OnValidate() for custom validation when values change in Inspector",
        "Use [System.Serializable] for custom classes to appear in Inspector",
        "ScriptableObject.CreateInstance() creates runtime instances without asset files",
        "Use [RequireComponent] to ensure required components are automatically added"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "scripting_best_practices", unity_scripting_knowledge)
    print("✅ Added Unity Scripting Best Practices")
    
    # Unity Performance Guidelines
    unity_performance_knowledge = [
        "Use GetComponent sparingly and cache references in Start() or Awake()",
        "Avoid Find() and FindObjectOfType() in Update() - cache references instead",
        "Use Object.Instantiate() with object pooling for frequently created objects",
        "Enable 'Static' flag for objects that don't move to enable batching",
        "Use SetActive() instead of Destroy() for frequently toggled objects",
        "Minimize garbage collection by avoiding string concatenation in loops",
        "Use Vector3.zero instead of new Vector3(0,0,0) to avoid allocation",
        "Enable 'Optimize Mesh Data' in model import settings for better performance",
        "Use LOD Groups for complex objects viewed at different distances",
        "Implement occlusion culling for large scenes with many objects"
    ]
    
    rag.add_to_knowledge_base("best_practices", "unity_performance", unity_performance_knowledge)
    print("✅ Added Unity Performance Guidelines")

def add_game_design_blog_knowledge():
    """Add knowledge from game design blogs and industry experts"""
    rag = RAGPipeline()
    
    # Game Feel and Player Experience
    game_feel_knowledge = [
        "Juicy feedback makes every action feel satisfying with visual and audio cues",
        "Screen shake adds impact to important events like explosions and hits",
        "Particle effects provide immediate visual feedback for player actions",
        "Sound design reinforces visual feedback and creates emotional responses",
        "Controller rumble enhances tactile feedback for console and mobile games",
        "Color coding helps players quickly understand game state and information",
        "Smooth animations with easing curves feel more natural than linear movement",
        "Anticipation frames prepare players for upcoming actions or events",
        "Follow-through animation continues movement slightly after input stops",
        "Squash and stretch animation principles add life to character movement"
    ]
    
    rag.add_to_knowledge_base("game_design", "game_feel", game_feel_knowledge)
    print("✅ Added Game Feel knowledge")
    
    # Player Psychology and Motivation
    psychology_knowledge = [
        "Variable reward schedules create addictive gameplay through unpredictable rewards",
        "Flow state occurs when challenge matches player skill level perfectly",
        "Mastery progression gives players long-term goals and skill development",
        "Social features like leaderboards and multiplayer increase engagement",
        "Narrative tension keeps players invested in story outcomes and character arcs",
        "Player agency allows meaningful choices that affect game world and story",
        "Cognitive load management prevents overwhelming players with too much information",
        "Progressive disclosure reveals complexity gradually as players learn",
        "Emotional investment through character development and relationship building",
        "Competence, autonomy, and relatedness are core psychological needs in games"
    ]
    
    rag.add_to_knowledge_base("game_design", "player_psychology", psychology_knowledge)
    print("✅ Added Player Psychology knowledge")

def add_industry_best_practices():
    """Add knowledge from industry best practices and standards"""
    rag = RAGPipeline()
    
    # Accessibility Standards
    accessibility_knowledge = [
        "Colorblind-friendly design uses patterns and shapes in addition to colors",
        "Adjustable text size accommodates players with visual impairments",
        "Remappable controls allow players to customize input to their needs",
        "Subtitles and closed captions make audio content accessible to all players",
        "High contrast modes help players distinguish game elements clearly",
        "Audio cues provide information for players with visual impairments",
        "One-handed play options accommodate players with limited mobility",
        "Seizure warnings and safe modes protect players with photosensitivity",
        "Difficulty options allow players to adjust challenge to their skill level",
        "Clear UI design with readable fonts and adequate spacing improves accessibility"
    ]
    
    rag.add_to_knowledge_base("best_practices", "accessibility", accessibility_knowledge)
    print("✅ Added Accessibility Standards")
    
    # Monetization and Business
    monetization_knowledge = [
        "Free-to-play models use psychological triggers for sustainable revenue",
        "Battle pass systems create recurring engagement and predictable revenue",
        "Cosmetic-only monetization maintains game balance while generating revenue",
        "Seasonal content updates keep players engaged and returning regularly",
        "Analytics tracking helps understand player behavior and optimize retention",
        "A/B testing different features helps optimize player engagement",
        "Live service games require ongoing content development and community management",
        "Premium pricing models work best for narrative-driven single-player experiences",
        "Subscription models provide predictable revenue for ongoing development",
        "Regional pricing adjusts costs to local purchasing power and market conditions"
    ]
    
    rag.add_to_knowledge_base("game_design", "monetization", monetization_knowledge)
    print("✅ Added Monetization knowledge")

def add_technical_standards():
    """Add knowledge from technical standards and industry practices"""
    rag = RAGPipeline()
    
    # Code Quality and Standards
    code_quality_knowledge = [
        "SOLID principles create maintainable and extensible code architecture",
        "Design patterns solve common programming problems in reusable ways",
        "Unit testing ensures code reliability and enables safe refactoring",
        "Code reviews catch bugs early and share knowledge across the team",
        "Documentation helps new developers understand and maintain existing code",
        "Version control with Git enables collaboration and tracks code history",
        "Continuous integration automates testing and deployment processes",
        "Code formatting standards improve readability and reduce merge conflicts",
        "Performance profiling identifies bottlenecks before they become problems",
        "Security best practices protect against common vulnerabilities and exploits"
    ]
    
    rag.add_to_knowledge_base("best_practices", "code_quality", code_quality_knowledge)
    print("✅ Added Code Quality Standards")
    
    # Platform-Specific Guidelines
    platform_guidelines_knowledge = [
        "App Store guidelines require specific UI patterns and content restrictions",
        "Google Play policies enforce similar but distinct requirements from iOS",
        "Steam requires specific store page formatting and community features",
        "Console certification processes have strict technical and content requirements",
        "WebGL builds need optimization for browser performance limitations",
        "Mobile games require touch-friendly UI and battery optimization",
        "PC games benefit from keyboard/mouse controls and scalable graphics",
        "VR games need 90+ FPS and motion sickness prevention techniques",
        "Switch development requires consideration of portable and docked modes",
        "Cross-platform development needs careful input and UI adaptation"
    ]
    
    rag.add_to_knowledge_base("best_practices", "platform_guidelines", platform_guidelines_knowledge)
    print("✅ Added Platform Guidelines")

def add_modern_game_trends():
    """Add knowledge about modern game development trends"""
    rag = RAGPipeline()
    
    # Modern Development Trends
    modern_trends_knowledge = [
        "Procedural generation creates infinite content and reduces development time",
        "Machine learning AI creates adaptive opponents and dynamic difficulty",
        "Cloud gaming enables high-end experiences on low-power devices",
        "Cross-platform play increases player base and reduces matchmaking time",
        "User-generated content extends game life and builds community engagement",
        "Seasonal content models provide regular updates and predictable revenue",
        "Battle royale mechanics create intense competition and social sharing",
        "Roguelike elements add replayability through procedural generation",
        "Social features like guilds and trading create persistent engagement",
        "Esports integration requires balanced competitive gameplay and spectator features"
    ]
    
    rag.add_to_knowledge_base("game_design", "modern_trends", modern_trends_knowledge)
    print("✅ Added Modern Game Trends")
    
    # Technology Trends
    tech_trends_knowledge = [
        "Ray tracing creates realistic lighting and reflections in real-time",
        "AI-powered animation reduces manual keyframing and creates natural movement",
        "Procedural audio generates dynamic soundscapes based on game events",
        "Cloud computing enables complex simulations and large-scale multiplayer",
        "5G networks reduce latency for mobile and cloud gaming experiences",
        "Blockchain enables true ownership of digital assets and cross-game items",
        "Augmented reality overlays game content on the real world",
        "Voice recognition allows natural language interaction with game systems",
        "Gesture controls provide intuitive interaction without physical controllers",
        "Haptic feedback creates tactile sensations for enhanced immersion"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "tech_trends", tech_trends_knowledge)
    print("✅ Added Technology Trends")

def main():
    """Add all external knowledge sources"""
    print("🌐 Adding Knowledge from External Sources")
    print("=" * 50)
    
    try:
        # Add Unity documentation knowledge
        add_unity_documentation_knowledge()
        
        # Add game design blog knowledge
        add_game_design_blog_knowledge()
        
        # Add industry best practices
        add_industry_best_practices()
        
        # Add technical standards
        add_technical_standards()
        
        # Add modern trends
        add_modern_game_trends()
        
        # Show final stats
        rag = RAGPipeline()
        stats = rag.get_knowledge_base_stats()
        print(f"\n📊 Final Knowledge Base Stats:")
        print(f"Total items: {stats['total_items']}")
        for category, count in stats['categories'].items():
            print(f"  {category}: {count} items")
        
        print("\n🎉 External knowledge addition completed successfully!")
        print("\nNew external knowledge categories added:")
        print("  ✅ Unity Scripting Best Practices")
        print("  ✅ Unity Performance Guidelines")
        print("  ✅ Game Feel & Player Experience")
        print("  ✅ Player Psychology & Motivation")
        print("  ✅ Accessibility Standards")
        print("  ✅ Monetization & Business")
        print("  ✅ Code Quality Standards")
        print("  ✅ Platform Guidelines")
        print("  ✅ Modern Game Trends")
        print("  ✅ Technology Trends")
        
        print("\n🌐 Sources Integrated:")
        print("  • Unity Official Documentation")
        print("  • Game Design Industry Blogs")
        print("  • Accessibility Standards (WCAG)")
        print("  • Platform Guidelines (App Store, Google Play, Steam)")
        print("  • Modern Development Trends")
        print("  • Industry Best Practices")
        
    except Exception as e:
        print(f"❌ Error adding external knowledge: {e}")

if __name__ == "__main__":
    main() 
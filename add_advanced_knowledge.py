#!/usr/bin/env python3
"""
Script to add advanced knowledge to the RAG system
Focuses on high-impact areas: Animation, Physics, Particles, Audio, Performance
"""

import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

from app.rag.rag_pipeline import RAGPipeline

def add_animation_knowledge():
    """Add comprehensive animation system knowledge"""
    rag = RAGPipeline()
    
    animation_knowledge = [
        "Animator Controller manages state machines for complex character animations",
        "Blend Trees smoothly transition between multiple animations based on parameters",
        "Animation Events trigger code execution at specific points in animations",
        "IK (Inverse Kinematics) creates realistic limb movement for characters",
        "Animation Curves allow fine-tuned control over animation timing and values",
        "Root Motion enables character movement driven by animation data",
        "Animation Layers allow multiple animations to play simultaneously",
        "Animation Override Controllers swap animations at runtime for different characters",
        "Animation Rigging provides advanced character setup and control",
        "Animation Compression reduces file size while maintaining quality"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "animation_systems", animation_knowledge)
    print("✅ Added Animation Systems knowledge")

def add_physics_knowledge():
    """Add comprehensive physics system knowledge"""
    rag = RAGPipeline()
    
    physics_knowledge = [
        "Rigidbody components enable realistic physics simulation for objects",
        "Colliders define the physical shape and boundaries of game objects",
        "Physics Materials control friction, bounciness, and other surface properties",
        "Joints connect objects together with constraints like hinges and springs",
        "Raycasting detects collisions along a line for shooting and detection",
        "Trigger colliders detect overlaps without physical collision response",
        "Physics layers allow selective collision detection between object groups",
        "Force and torque can be applied to create realistic object movement",
        "Cloth simulation creates realistic fabric movement for clothing and flags",
        "Terrain colliders provide efficient collision for large landscape objects"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "physics_systems", physics_knowledge)
    print("✅ Added Physics Systems knowledge")

def add_particle_knowledge():
    """Add comprehensive particle system knowledge"""
    rag = RAGPipeline()
    
    particle_knowledge = [
        "Particle Systems create visual effects like explosions, fire, and magic",
        "VFX Graph provides node-based visual effects for complex particle systems",
        "Emission modules control how and when particles are spawned",
        "Shape modules define the area where particles are emitted from",
        "Velocity modules control particle movement and direction",
        "Color over Lifetime creates dynamic color changes during particle lifetime",
        "Size over Lifetime allows particles to grow or shrink over time",
        "Force fields create areas that affect particle movement and behavior",
        "Sub-emitters spawn additional particles when main particles die",
        "Particle collision enables particles to interact with game world objects"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "particle_systems", particle_knowledge)
    print("✅ Added Particle Systems knowledge")

def add_audio_knowledge():
    """Add comprehensive audio system knowledge"""
    rag = RAGPipeline()
    
    audio_knowledge = [
        "Audio Mixer provides advanced audio routing and effects processing",
        "Spatial Audio creates 3D sound positioning for immersive experiences",
        "Audio Filters like low-pass and high-pass create dynamic sound effects",
        "Audio Reverb Zones simulate realistic acoustic environments",
        "Audio Doppler Effect creates realistic sound changes for moving objects",
        "Audio Occlusion blocks sound through walls and obstacles",
        "Audio Compression reduces file size while maintaining sound quality",
        "Audio Streaming loads audio files progressively to save memory",
        "Audio Visualization creates real-time visual representations of sound",
        "Audio Ducking automatically lowers background music during dialogue"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "audio_systems", audio_knowledge)
    print("✅ Added Audio Systems knowledge")

def add_performance_knowledge():
    """Add comprehensive performance optimization knowledge"""
    rag = RAGPipeline()
    
    performance_knowledge = [
        "Object Pooling reuses objects instead of creating and destroying them",
        "LOD (Level of Detail) reduces polygon count for distant objects",
        "Occlusion Culling hides objects that are not visible to the camera",
        "Texture Streaming loads high-resolution textures only when needed",
        "GPU Instancing renders multiple objects with a single draw call",
        "Static Batching combines static objects to reduce draw calls",
        "Dynamic Batching automatically batches small dynamic objects",
        "Memory Profiling identifies memory leaks and optimization opportunities",
        "Frame Rate Optimization targets consistent 60 FPS for smooth gameplay",
        "Build Optimization reduces final game size and improves loading times"
    ]
    
    rag.add_to_knowledge_base("best_practices", "performance_optimization", performance_knowledge)
    print("✅ Added Performance Optimization knowledge")

def add_ai_ml_knowledge():
    """Add AI and machine learning knowledge"""
    rag = RAGPipeline()
    
    ai_ml_knowledge = [
        "Unity ML-Agents enables machine learning for game AI and behavior",
        "Behavior Trees create complex AI decision-making systems",
        "NavMesh provides automatic pathfinding for AI characters",
        "State Machines manage AI behavior transitions and logic",
        "Decision Trees create branching AI logic based on game conditions",
        "Neural Networks can be trained for adaptive AI behavior",
        "Reinforcement Learning allows AI to learn from player interactions",
        "Procedural AI generates dynamic behavior patterns and responses",
        "AI Perception systems detect and respond to player actions",
        "AI Memory systems remember past events and player behavior patterns"
    ]
    
    rag.add_to_knowledge_base("game_design", "ai_ml_systems", ai_ml_knowledge)
    print("✅ Added AI/ML Systems knowledge")

def add_networking_knowledge():
    """Add networking and multiplayer knowledge"""
    rag = RAGPipeline()
    
    networking_knowledge = [
        "Client-Server architecture separates game logic from player input",
        "Peer-to-Peer networking allows direct connections between players",
        "Network synchronization keeps game state consistent across all players",
        "Lag compensation predicts player actions to reduce perceived delay",
        "Network prediction smooths movement and reduces jitter",
        "Authority systems determine which client controls specific game objects",
        "Network events efficiently transmit game state changes",
        "Room-based matchmaking groups players into game sessions",
        "Cross-platform networking enables play between different devices",
        "Network security prevents cheating and ensures fair gameplay"
    ]
    
    rag.add_to_knowledge_base("game_design", "networking", networking_knowledge)
    print("✅ Added Networking knowledge")

def add_vr_ar_knowledge():
    """Add VR/AR development knowledge"""
    rag = RAGPipeline()
    
    vr_ar_knowledge = [
        "XR Toolkit provides cross-platform VR/AR development framework",
        "Hand tracking enables natural interaction without controllers",
        "Eye tracking creates immersive experiences based on gaze direction",
        "Spatial audio creates realistic 3D sound positioning in VR",
        "Room-scale VR allows players to move physically in virtual space",
        "Haptic feedback provides tactile sensations for enhanced immersion",
        "VR locomotion systems prevent motion sickness during movement",
        "AR plane detection identifies real-world surfaces for object placement",
        "Mixed reality combines virtual and real-world elements seamlessly",
        "VR optimization targets 90+ FPS for comfortable virtual experiences"
    ]
    
    rag.add_to_knowledge_base("unity_specific", "vr_ar_development", vr_ar_knowledge)
    print("✅ Added VR/AR Development knowledge")

def add_mobile_knowledge():
    """Add mobile development knowledge"""
    rag = RAGPipeline()
    
    mobile_knowledge = [
        "Touch controls provide intuitive interaction for mobile devices",
        "Gesture recognition enables swipe, pinch, and multi-touch actions",
        "Mobile optimization targets 30-60 FPS on various device capabilities",
        "Battery optimization reduces power consumption for longer play sessions",
        "Memory management is critical for devices with limited RAM",
        "App store guidelines must be followed for successful publication",
        "Mobile UI design prioritizes thumb-friendly interface elements",
        "Cloud saves enable cross-device progress synchronization",
        "Mobile analytics track user behavior and app performance",
        "Push notifications re-engage players and increase retention"
    ]
    
    rag.add_to_knowledge_base("best_practices", "mobile_development", mobile_knowledge)
    print("✅ Added Mobile Development knowledge")

def main():
    """Add all advanced knowledge categories"""
    print("🚀 Adding Advanced Knowledge to RAG System")
    print("=" * 55)
    
    try:
        # Add Unity-specific advanced knowledge
        add_animation_knowledge()
        add_physics_knowledge()
        add_particle_knowledge()
        add_audio_knowledge()
        add_vr_ar_knowledge()
        
        # Add game design advanced knowledge
        add_ai_ml_knowledge()
        add_networking_knowledge()
        
        # Add best practices advanced knowledge
        add_performance_knowledge()
        add_mobile_knowledge()
        
        # Show final stats
        rag = RAGPipeline()
        stats = rag.get_knowledge_base_stats()
        print(f"\n📊 Final Knowledge Base Stats:")
        print(f"Total items: {stats['total_items']}")
        for category, count in stats['categories'].items():
            print(f"  {category}: {count} items")
        
        print("\n🎉 Advanced knowledge addition completed successfully!")
        print("\nNew advanced categories added:")
        print("  ✅ Animation Systems")
        print("  ✅ Physics Systems")
        print("  ✅ Particle Systems")
        print("  ✅ Audio Systems")
        print("  ✅ Performance Optimization")
        print("  ✅ AI/ML Systems")
        print("  ✅ Networking")
        print("  ✅ VR/AR Development")
        print("  ✅ Mobile Development")
        
        print("\n🎯 Impact:")
        print("  • 80+ new advanced technical concepts")
        print("  • Modern game development workflows")
        print("  • Cutting-edge Unity features")
        print("  • Performance and optimization best practices")
        
    except Exception as e:
        print(f"❌ Error adding advanced knowledge: {e}")

if __name__ == "__main__":
    main() 
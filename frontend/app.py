"""
AI Unity Game Prototype Generator - Streamlit Frontend
A simple web interface for generating Unity game prototypes
"""

import streamlit as st
import requests
import json
import time
from typing import Dict, List, Any

# Configuration
BACKEND_URL = "http://localhost:8000"

def main():
    st.set_page_config(
        page_title="AI Unity Game Generator",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .enhancement-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #c3e6cb;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #f5c6cb;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🎮 AI Unity Game Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transform your game idea into a complete Unity prototype with AI-powered enhancements</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🚀 Quick Start")
        st.markdown("""
        1. **Describe your game idea** in the text area
        2. **Select a genre** (optional)
        3. **Review AI suggestions** and choose what to include
        4. **Generate your Unity project** and download it!
        """)
        
        st.header("📋 Supported Genres")
        genres = [
            "Platformer", "RPG", "Puzzle", "Shooter", 
            "Adventure", "Strategy", "Racing", "General"
        ]
        st.write(", ".join(genres))
        
        st.header("🔧 Features")
        st.markdown("""
        ✅ **AI-powered enhancements**
        ✅ **Unity C# code generation**
        ✅ **Project structure creation**
        ✅ **Ready-to-import prototypes**
        ✅ **Multiple game genres**
        """)
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["🎯 Game Idea", "✨ Enhancements", "📦 Generate Project"])
    
    with tab1:
        st.header("Describe Your Game Idea")
        
        # Game idea input
        game_idea = st.text_area(
            "What's your game idea?",
            placeholder="e.g., A 2D platformer where a fox collects magical gems to restore a forest...",
            height=150,
            help="Be as detailed as you want! The AI will use this to suggest improvements."
        )
        
        # Genre selection
        col1, col2 = st.columns(2)
        with col1:
            genre = st.selectbox(
                "Game Genre (Optional)",
                ["general", "platformer", "rpg", "puzzle", "shooter", "adventure", "strategy", "racing"],
                help="This helps the AI provide more relevant suggestions"
            )
        
        with col2:
            st.write("")
            st.write("")
            if st.button("🚀 Enhance My Idea", type="primary", use_container_width=True):
                if game_idea.strip():
                    enhance_game_idea(game_idea, genre)
                else:
                    st.error("Please enter a game idea first!")
    
    with tab2:
        st.header("AI Enhancements")
        
        # Display enhancements if available
        if "enhancements" in st.session_state:
            display_enhancements()
        else:
            st.info("👆 Go to the 'Game Idea' tab and enhance your idea to see suggestions here!")
    
    with tab3:
        st.header("Generate Unity Project")
        
        if "enhancements" in st.session_state and "selected_enhancements" in st.session_state:
            display_project_generation()
        else:
            st.info("👆 Complete the enhancement step first to generate your project!")

def enhance_game_idea(game_idea: str, genre: str):
    """Call the backend to enhance the game idea"""
    
    with st.spinner("🤖 AI is analyzing your game idea..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/enhance-idea",
                json={"description": game_idea, "genre": genre},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                st.session_state.enhancements = data["enhancements"]
                st.session_state.original_idea = data["original_idea"]
                st.session_state.selected_enhancements = {}
                st.success("✅ AI enhancements generated successfully!")
                st.rerun()
            else:
                st.error(f"❌ Error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {str(e)}")
            st.info("💡 Make sure the backend server is running on localhost:8000")

def display_enhancements():
    """Display the AI enhancements with checkboxes"""
    
    st.markdown(f"**Original Idea:** {st.session_state.original_idea}")
    st.divider()
    
    # Create a form for enhancements
    with st.form("enhancements_form"):
        st.subheader("Select the enhancements you want to include:")
        
        for enhancement in st.session_state.enhancements:
            st.markdown(f"### {enhancement['category'].title()}")
            st.markdown(f"*{enhancement['description']}*")
            
            # Create checkboxes for each suggestion
            selected_suggestions = []
            for suggestion in enhancement['suggestions']:
                if st.checkbox(suggestion, key=f"{enhancement['category']}_{suggestion}"):
                    selected_suggestions.append(suggestion)
            
            st.session_state.selected_enhancements[enhancement['category']] = selected_suggestions
            
            st.divider()
        
        if st.form_submit_button("✅ Confirm Selections", type="primary"):
            st.success("✅ Enhancements selected! Go to the 'Generate Project' tab to create your Unity project.")
            st.rerun()

def display_project_generation():
    """Display project generation interface"""
    
    st.markdown("### Selected Enhancements:")
    for category, suggestions in st.session_state.selected_enhancements.items():
        if suggestions:
            st.markdown(f"**{category.title()}:** {', '.join(suggestions)}")
    
    st.divider()
    
    if st.button("🎮 Generate Unity Project", type="primary", use_container_width=True):
        generate_unity_project()

def generate_unity_project():
    """Call the backend to generate the Unity project"""
    
    with st.spinner("🔨 Generating your Unity project..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/generate-project",
                json={
                    "original_idea": st.session_state.original_idea,
                    "selected_enhancements": st.session_state.selected_enhancements
                },
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Display project info
                st.success("✅ Unity project generated successfully!")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Files Generated", data["file_count"])
                with col2:
                    st.metric("Main Scripts", len(data["main_scripts"]))
                with col3:
                    st.metric("Project Size", "~2-5 MB")
                
                # Display generated scripts
                st.subheader("Generated C# Scripts:")
                for script in data["main_scripts"]:
                    st.code(f"Assets/Scripts/{script}.cs", language="text")
                
                # Download button (in a real app, this would download the actual file)
                st.markdown("---")
                st.markdown("### 📥 Download Your Project")
                st.info("""
                **Note:** In this demo, the project is generated but not actually downloadable.
                In a full implementation, you would get a real Unity project zip file!
                
                To test this locally:
                1. Check the backend console for the generated project path
                2. Look for a zip file in the backend directory
                3. Extract and open in Unity
                """)
                
                # Simulate download button
                if st.button("📦 Download Unity Project (Demo)", use_container_width=True):
                    st.balloons()
                    st.success("🎉 Project ready! (This is a demo - check the backend for the actual file)")
                
            else:
                st.error(f"❌ Error generating project: {response.text}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {str(e)}")

def check_backend_health():
    """Check if the backend is running"""
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False

if __name__ == "__main__":
    # Check backend health
    if not check_backend_health():
        st.error("""
        ❌ **Backend server is not running!**
        
        To start the backend:
        1. Open a terminal
        2. Navigate to the backend directory
        3. Run: `uvicorn app.main:app --reload`
        4. Make sure you have set your OPENAI_API_KEY in a .env file
        """)
        st.stop()
    
    main() 
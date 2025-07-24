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
            "Adventure", "Strategy", "Racing", "Metroidvania", "Roguelike", "Survival", "Puzzle-Platformer", "3D Platformer", "3D Adventure", "3D Shooter", "3D Puzzle", "General"
        ]
        st.write(", ".join(genres))
        
        st.header("🔧 Features")
        st.markdown("""
        ✅ **AI-powered enhancements**
        ✅ **Unity C# code generation**
        ✅ **Project structure creation**
        ✅ **Ready-to-import prototypes**
        ✅ **Multiple game genres**
        ✅ **New: Audio, Visual Effects, UI/UX, Cutscenes enhancements**
        """)
    
    # Main content
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Game Idea", "✨ Enhancements", "📦 Generate Project", "💬 Chat"])
    
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
                ["general", "platformer", "rpg", "puzzle", "shooter", "adventure", "strategy", "racing", "metroidvania", "roguelike", "survival", "puzzle-platformer", "3d platformer", "3d adventure", "3d shooter", "3d puzzle"],
                help="This helps the AI provide more relevant suggestions"
            )
            st.session_state["selected_genre"] = genre
        
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

    with tab4:
        st.header("💬 Chat with Unity AI Assistant")
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []
        for entry in st.session_state["chat_history"]:
            if entry["role"] == "user":
                st.markdown(f"<div style='text-align:right'><b>You:</b> {entry['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align:left'><b>Assistant:</b> {entry['content']}</div>", unsafe_allow_html=True)
        user_input = st.text_input("Type your message...", key="chat_input")
        if st.button("Send", key="send_chat"):
            if user_input.strip():
                st.session_state["chat_history"].append({"role": "user", "content": user_input})
                with st.spinner("Assistant is typing..."):
                    try:
                        resp = requests.post(f"{BACKEND_URL}/chat", json={"message": user_input}, timeout=60)
                        if resp.status_code == 200:
                            data = resp.json()
                            st.session_state["chat_history"].append({"role": "assistant", "content": data["response"]})
                        else:
                            st.session_state["chat_history"].append({"role": "assistant", "content": f"Error: {resp.text}"})
                    except Exception as e:
                        st.session_state["chat_history"].append({"role": "assistant", "content": f"Error: {str(e)}"})
                st.experimental_rerun()

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
    
    # Asset Generation Modal Logic
    if "show_asset_modal" not in st.session_state:
        st.session_state["show_asset_modal"] = False
    
    if st.button("🖼️ Generate Assets (Optional)", use_container_width=True):
        st.session_state["show_asset_modal"] = True
        st.experimental_rerun()
    
    if st.session_state["show_asset_modal"]:
        with st.expander("AI Asset Generation", expanded=True):
            st.markdown("**Select which assets to generate and which AI model(s) to use:**")
            with st.form("asset_generation_form"):
                asset_types = st.multiselect(
                    "Asset Types",
                    ["Main Character", "Enemy", "Background", "Icon"],
                    default=["Main Character", "Enemy"]
                )
                model_choices = st.multiselect(
                    "AI Model(s)",
                    ["DALL·E", "Stable Diffusion"],
                    default=["DALL·E"]
                )
                asset_descriptions = {}
                for asset_type in asset_types:
                    asset_descriptions[asset_type] = st.text_input(
                        f"Description for {asset_type}",
                        value="" if asset_type not in st.session_state.get("last_asset_descriptions", {}) else st.session_state["last_asset_descriptions"][asset_type],
                        key=f"desc_{asset_type}"
                    )
                generate = st.form_submit_button("Generate Assets", type="primary")
                cancel = st.form_submit_button("Cancel")
                if generate:
                    st.session_state["selected_asset_types"] = asset_types
                    st.session_state["selected_asset_models"] = model_choices
                    st.session_state["last_asset_descriptions"] = asset_descriptions
                    st.session_state["show_asset_modal"] = False
                    # Call backend to generate assets
                    with st.spinner("Generating assets with AI..."):
                        try:
                            response = requests.post(
                                f"{BACKEND_URL}/generate-assets",
                                json={
                                    "asset_types": asset_types,
                                    "asset_descriptions": asset_descriptions,
                                    "models": model_choices,
                                    "game_description": st.session_state.get("original_idea", ""),
                                    "genre": st.session_state.get("selected_genre", st.session_state.get("genre", "general")),
                                    "project_folder_name": st.session_state.get("project_folder_name", "")
                                },
                                timeout=60
                            )
                            if response.status_code == 200:
                                data = response.json()
                                st.success(f"{data.get('message','Assets generated!')}")
                                if data.get('generated_files'):
                                    st.markdown("**Generated Files:**")
                                    for f in data['generated_files']:
                                        st.write(f)
                                        if f.endswith('.png'):
                                            try:
                                                st.image(f, caption=f, use_column_width=True)
                                            except Exception:
                                                pass
                            else:
                                st.error(f"❌ Error: {response.text}")
                        except requests.exceptions.RequestException as e:
                            st.error(f"❌ Connection error: {str(e)}")
                if cancel:
                    st.session_state["show_asset_modal"] = False
                    st.experimental_rerun()
    
    if st.button("🎮 Generate Unity Project", type="primary", use_container_width=True):
        generate_unity_project()
    
    # Show download link if available
    if "last_project_url" in st.session_state and "last_project_filename" in st.session_state:
        st.success("✅ Unity project generated! Click below to download your .zip file.")
        download_url = f"{BACKEND_URL}/download/{st.session_state['last_project_filename']}"
        st.markdown(f"[📦 Download Unity Project]({download_url})", unsafe_allow_html=True)

def generate_unity_project():
    """Call the backend to generate the Unity project"""
    
    with st.spinner("🔨 Generating your Unity project..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/generate-project",
                json={
                    "original_idea": st.session_state.original_idea,
                    "selected_enhancements": st.session_state.selected_enhancements,
                    "genre": st.session_state.get("selected_genre", st.session_state.get("genre", "general"))
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
                
                # Save project folder name for asset generation
                if "project_url" in data and data["project_url"].startswith("/downloads/"):
                    filename = data["project_url"].split("/")[-1]
                    st.session_state["last_project_url"] = data["project_url"]
                    st.session_state["last_project_filename"] = filename
                    # Extract project folder name from filename (strip .zip)
                    if filename.endswith(".zip"):
                        folder_name = filename[:-4]
                        st.session_state["project_folder_name"] = folder_name
                
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
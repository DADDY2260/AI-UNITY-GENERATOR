"""
AI Unity Game Prototype Generator - Streamlit Frontend
A simple web interface for generating Unity game prototypes.

This module defines the Streamlit frontend for the AI Unity Game Generator.
It provides a user-friendly interface for describing game ideas, reviewing AI enhancements,
generating Unity projects, chatting with an AI assistant, and managing assets.
"""

import streamlit as st
import requests
import json
import time
from typing import Dict, List, Any

# Configuration
BACKEND_URL = "http://127.0.0.1:8000"  # Use IP instead of localhost

def main():
    """
    Main entry point for the Streamlit frontend UI.
    Sets up the page, sidebar, and main tabs for game idea input, enhancements, project generation, and chat.
    """
    st.set_page_config(
        page_title="AI Unity Game Generator",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Add debugging after set_page_config
    st.write(f"🔍 Checking backend at: {BACKEND_URL}")
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    /* Main header styling */
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.3rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Card styling for enhancements */
    .enhancement-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin: 0.8rem 0;
        border: 1px solid #dee2e6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
    }
    .enhancement-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Success and error message styling */
    .success-message {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        color: #155724;
        padding: 1.2rem;
        border-radius: 0.8rem;
        border: 1px solid #c3e6cb;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .error-message {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        color: #721c24;
        padding: 1.2rem;
        border-radius: 0.8rem;
        border: 1px solid #f5c6cb;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Chat message styling */
    .chat-user {
        background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
        color: white;
        padding: 0.8rem 1.2rem;
        border-radius: 1rem 1rem 0.2rem 1rem;
        margin: 0.5rem 0;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .chat-assistant {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        color: #333;
        padding: 0.8rem 1.2rem;
        border-radius: 1rem 1rem 1rem 0.2rem;
        margin: 0.5rem 0;
        max-width: 80%;
        border: 1px solid #dee2e6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 0.5rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        border-radius: 0.5rem;
        border: 2px solid #dee2e6;
        transition: border-color 0.2s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #007bff;
        box-shadow: 0 0 0 0.2rem rgba(0,123,255,0.25);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        .sub-header {
            font-size: 1.1rem;
        }
    }
    
    /* Loading spinner styling */
    .loading-container {
        text-align: center;
        padding: 2rem;
    }
    
    /* Tooltip styling */
    .tooltip {
        position: relative;
        display: inline-block;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
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
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Game Idea", "✨ Elements", "📦 Generate Project", "💬 Chat"])
    
    with tab1:
        st.header("Describe Your Game Idea")
        
        # Game idea input with better UX
        game_idea = st.text_area(
            "What's your game idea?",
            placeholder="e.g., A 2D platformer where a fox collects magical gems to restore a forest...",
            height=150,
            help="Be as detailed as you want! The AI will use this to suggest improvements. Include genre, mechanics, story elements, or any specific features you want."
        )
        
        # Example prompts for inspiration
        with st.expander("💡 Need inspiration? Try these examples:", expanded=False):
            st.markdown("""
            **Platformer Examples:**
            - "A 2D platformer where a robot explores an abandoned space station"
            - "A 3D platformer where a cat jumps between floating islands"
            
            **RPG Examples:**
            - "A turn-based RPG where you manage a small village"
            - "An action RPG where you play as a time-traveling knight"
            
            **Shooter Examples:**
            - "A top-down shooter where you defend a base from waves of enemies"
            - "A first-person shooter set in a cyberpunk city"
            """)
        
        # Genre selection with better organization
        col1, col2 = st.columns(2)
        with col1:
            genre = st.selectbox(
                "Game Genre (Optional)",
                ["general", "platformer", "rpg", "puzzle", "shooter", "adventure", "strategy", "racing", "metroidvania", "roguelike", "survival", "puzzle-platformer", "3d platformer", "3d adventure", "3d shooter", "3d puzzle"],
                help="This helps the AI provide more relevant suggestions. Choose 'general' if you're unsure!"
            )
            st.session_state["selected_genre"] = genre
        
        with col2:
            st.write("")
            st.write("")
            if st.button("🚀 Enhance My Idea", type="primary", use_container_width=True, help="Send your idea to the AI for enhancement suggestions"):
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
        st.markdown("""
        <div class="chat-header">
            <h2>💬 Chat with AI Unity Assistant</h2>
            <p>Ask me anything about Unity game development, C# scripting, or game design!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Example prompts
        with st.expander("💡 Example Questions", expanded=False):
            st.markdown("""
            **Try asking:**
            - "How do I make a player controller in Unity?"
            - "What's the best way to handle collision detection?"
            - "How can I optimize my game's performance?"
            - "What are some good practices for Unity project structure?"
            - "How do I create a simple inventory system?"
            - "What's the difference between Update() and FixedUpdate()?"
            """)
        
        # Chat interface
        if "chat_messages" not in st.session_state:
            st.session_state.chat_messages = []
        
        # Display chat history with improved styling
        for entry in st.session_state["chat_messages"]:
            if entry["role"] == "user":
                st.markdown(f'<div class="chat-user"><b>You:</b> {entry["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-assistant"><b>Assistant:</b> {entry["content"]}</div>', unsafe_allow_html=True)
        
        # Chat input with better UX
        user_input = st.text_input(
            "Type your message...", 
            key="chat_input",
            placeholder="Ask about Unity development, game mechanics, or code examples..."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Send", key="send_chat", help="Send your message to the AI assistant"):
                if user_input.strip():
                    st.session_state["chat_messages"].append({"role": "user", "content": user_input})
                    with st.spinner("🤖 Assistant is thinking..."):
                        try:
                            resp = requests.post(f"{BACKEND_URL}/chat", json={"message": user_input}, timeout=60)
                            if resp.status_code == 200:
                                data = resp.json()
                                st.session_state["chat_messages"].append({"role": "assistant", "content": data["response"]})
                            else:
                                st.session_state["chat_messages"].append({"role": "assistant", "content": f"❌ Error: {resp.text}"})
                        except Exception as e:
                            st.session_state["chat_messages"].append({"role": "assistant", "content": f"❌ Connection error: {str(e)}"})
                    st.experimental_rerun()
                else:
                    st.warning("Please enter a message first!")
        
        with col2:
            if st.button("Clear Chat", key="clear_chat", help="Clear the chat history"):
                st.session_state["chat_messages"] = []
                st.experimental_rerun()

def enhance_game_idea(game_idea: str, genre: str):
    """
    Call the backend to enhance the user's game idea using LLM and RAG.
    Updates session state with enhancements and original idea.
    """
    
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
    """
    Display the AI enhancements with checkboxes for user selection.
    Updates session state with selected enhancements.
    """
    st.markdown(f"**Original Idea:** {st.session_state.original_idea}")
    st.divider()
    
    # Create a form for enhancements with better visual organization
    with st.form("enhancements_form"):
        st.subheader("Select the enhancements you want to include:")
        st.info("💡 Check the boxes for features you want in your Unity project. You can select multiple items from each category!")
        
        for enhancement in st.session_state.enhancements:
            # Create a card-like container for each enhancement category
            with st.container():
                st.markdown(f"### 🎯 {enhancement['category'].title()}")
                st.markdown(f"*{enhancement['description']}*")
                
                # Create checkboxes for each suggestion with better spacing
                selected_suggestions = []
                for i, suggestion in enumerate(enhancement['suggestions']):
                    if st.checkbox(
                        suggestion, 
                        key=f"{enhancement['category']}_{suggestion}",
                        help=f"Add {suggestion} to your Unity project"
                    ):
                        selected_suggestions.append(suggestion)
                
                st.session_state.selected_enhancements[enhancement['category']] = selected_suggestions
                
                # Show selection summary
                if selected_suggestions:
                    st.success(f"✅ Selected: {', '.join(selected_suggestions)}")
                else:
                    st.info("No items selected from this category")
                
                st.divider()
        
        # Form submission with better feedback
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.form_submit_button("✅ Confirm Selections", type="primary", help="Save your selections and proceed to project generation"):
                total_selected = sum(len(suggestions) for suggestions in st.session_state.selected_enhancements.values())
                if total_selected > 0:
                    st.success(f"✅ {total_selected} enhancements selected! Go to the 'Generate Project' tab to create your Unity project.")
                else:
                    st.warning("⚠️ No enhancements selected. You can still generate a basic Unity project, or go back and select some features!")
                st.rerun()
        
        with col2:
            if st.form_submit_button("🔄 Reset All", help="Clear all selections and start over"):
                st.session_state.selected_enhancements = {}
                st.rerun()

def display_project_generation():
    """
    Display the project generation interface, including selected enhancements,
    asset generation modal, and download link for the generated Unity project.
    """
    
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
    """
    Call the backend to generate the Unity project based on the user's selections.
    Updates session state with project info and download link.
    """
    
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
    """
    Check if the backend server is running and healthy.
    Returns True if healthy, False otherwise.
    """
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        return response.status_code == 200
    except Exception as e:
        return False

if __name__ == "__main__":
    # Check backend health before launching the app
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
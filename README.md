# 🚀 AI Unity Game Prototype Generator

An AI-powered assistant that transforms your game idea into a complete, ready-to-import Unity prototype—code, project structure, and creative enhancements included.

---

## ✨ Why This Project?
This project demonstrates advanced skills in:
- **AI/NLP integration** (LLMs, RAG, prompt engineering)
- **Full-stack development** (FastAPI backend, Streamlit frontend)
- **Automated code generation** (Unity C# scripts, project packaging)
- **User-centric design** (conversational UI, extensible features)

Built to showcase how AI can accelerate game development and empower creators.

---

## 🖼️ Screenshots & Demo
<!--
Add screenshots or GIFs here to show the UI and generated Unity project structure.
Example:
![Web UI Screenshot](screenshots/ui.png)
![Unity Project Structure](screenshots/unity_project.png)
-->

---

## 🏗️ How It Works (Architecture)
1. **User Input:** Describe your game idea in plain English.
2. **AI Enhancement:** LLM + RAG pipeline suggests mechanics, levels, story, and more.
3. **Code Generation:** Backend creates Unity C# scripts and project folders using Jinja2 templates.
4. **Download:** Get a .zip file with a complete Unity project, ready to open in the Unity Editor.

```
[User] → [Streamlit Frontend] → [FastAPI Backend]
    ↳ [LLM + RAG] → [Unity Code Generator] → [Project Packaging]
```

---

## 💡 Resume-Ready Project Highlights
- **AI-powered Unity code assistant:** Converts natural language ideas into working Unity projects.
- **Retrieval-Augmented Generation:** Uses a custom knowledge base to improve suggestions.
- **Full-stack solution:** FastAPI backend, Streamlit frontend, modular and extensible.
- **Automated asset and script generation:** Supports multiple genres, mechanics, and features.
- **Modern Python best practices:** Async, type hints, docstrings, and code formatting.

---

## 📁 Project Structure
```
ai-unity-generator/
├── backend/                 # FastAPI backend with LLM integration
│   ├── app/
│   │   ├── main.py         # FastAPI server
│   │   ├── llm/            # LLM integration
│   │   ├── generators/     # Code generation logic
│   │   └── templates/      # Unity code templates
├── frontend/               # Streamlit web interface
│   └── app.py
├── requirements.txt        # Python dependencies
├── start_backend.py       # Backend startup script
├── start_frontend.py      # Frontend startup script
├── SETUP.md               # Detailed setup guide
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key ([get one](https://platform.openai.com/api-keys))
- Unity 2020+ (for testing generated projects)

### Installation
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set up environment:**
   ```bash
   cp env.example .env  # or copy manually
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_actual_api_key_here
   ```
3. **Test your setup:**
   ```bash
   python dev_scripts/test_setup.py
   ```
4. **Run the application:**
   ```bash
   # Terminal 1: Start backend
   python start_backend.py
   # Terminal 2: Start frontend
   python start_frontend.py
   ```
5. **Open your browser:** Go to `http://localhost:8501`

---

## 🎮 Example Usage
1. Open the web interface at `http://localhost:8501`
2. Enter: "2D platformer where a fox collects gems"
3. Review AI suggestions:
   - **Mechanics:** Double jump, wall climbing, collectible system
   - **Levels:** Secret rooms, boss battles, checkpoint system
   - **Story:** Fox seeks magical artifact, forest restoration
4. Select enhancements you want to include
5. Generate Unity project with complete C# scripts
6. Download and import into Unity!

---

## 🔧 Features
- ✅ **AI-Powered Enhancements:** Get creative suggestions for your game idea
- ✅ **Unity Code Generation:** Complete C# scripts ready for Unity
- ✅ **Project Structure:** Proper Unity folder organization
- ✅ **Multiple Genres:** Platformer, RPG, Puzzle, Shooter, and more
- ✅ **Beginner-Friendly:** Simple web interface with Streamlit
- ✅ **Extensible:** Easy to add new templates and features

---

## 📚 Documentation
- **[SETUP.md](SETUP.md):** Detailed setup and troubleshooting guide
- **[DEPLOYMENT.md](DEPLOYMENT.md):** Complete deployment guide (Docker, Render, Railway, Heroku, VPS)
- **[QUICK_DEPLOY.md](QUICK_DEPLOY.md):** Quick deployment reference
- **Backend API:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

## 🚀 Deployment

This project can be deployed to various platforms:

- **🐳 Docker**: `docker-compose up -d` (see [DEPLOYMENT.md](DEPLOYMENT.md))
- **☁️ Render**: Free tier available, automatic SSL (see [render.yaml](render.yaml))
- **🚂 Railway**: Simple deployment with auto-detection
- **🌐 Heroku**: Traditional PaaS deployment
- **💻 VPS**: Self-hosted on any Linux server

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for detailed instructions on all deployment methods.

---

## 📝 License
MIT License - feel free to use and modify!

---

**🎉 Ready to create your first AI-generated Unity game? Follow the setup guide and start building!** 
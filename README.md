# 🚀 AI Unity Game Prototype Generator

An AI-powered tool that takes your game idea and generates a complete Unity prototype with code, configurations, and suggestions.

## 🎯 What This Does

1. **Input**: You describe your game idea (e.g., "2D platformer where a fox collects gems")
2. **AI Enhancement**: Suggests mechanics, levels, and story elements
3. **Code Generation**: Creates Unity C# scripts and project structure
4. **Output**: Ready-to-import Unity prototype

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
├── test_setup.py          # Setup verification script
├── env.example            # Environment template
├── SETUP.md               # Detailed setup guide
└── README.md
```

## 🛠 Tech Stack

- **Backend**: FastAPI + OpenAI API
- **Frontend**: Streamlit (simple and beginner-friendly)
- **Code Generation**: Jinja2 templates + LLM
- **Game Target**: Unity C# (2020+ compatible)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (get one from [OpenAI Platform](https://platform.openai.com/api-keys))
- Unity 2020+ (for testing generated projects)

### Installation

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set up environment**:
```bash
# Copy environment template
cp env.example .env

# Edit .env and add your OpenAI API key
OPENAI_API_KEY=your_actual_api_key_here
```

3. **Test your setup**:
```bash
python test_setup.py
```

4. **Run the application**:
```bash
# Terminal 1: Start backend
python start_backend.py

# Terminal 2: Start frontend  
python start_frontend.py
```

5. **Open your browser** and go to: `http://localhost:8501`

## 📋 Development Phases

- ✅ **Phase 1**: Core LLM functionality (Week 1-2) - **COMPLETED**
- ✅ **Phase 2**: Code skeleton generation (Week 2-3) - **COMPLETED**
- ✅ **Phase 3**: Frontend + interaction (Week 3-4) - **COMPLETED**
- 🗹 **Phase 4**: Placeholder asset generation (Week 4-5)
- 🗹 **Phase 5**: Packaging + deployment (Week 5-6)

## 🎮 Example Usage

1. Open the web interface at `http://localhost:8501`
2. Enter: "2D platformer where a fox collects gems"
3. Review AI suggestions:
   - **Mechanics**: Double jump, wall climbing, collectible system
   - **Levels**: Secret rooms, boss battles, checkpoint system
   - **Story**: Fox seeks magical artifact, forest restoration
4. Select enhancements you want to include
5. Generate Unity project with complete C# scripts
6. Download and import into Unity!

## 🔧 Generated Unity Scripts

The system generates these Unity C# scripts:

- **PlayerController.cs**: Movement, jumping, input handling
- **GameManager.cs**: Game state, scoring, level management
- **UIManager.cs**: User interface and menu systems
- **Collectible.cs**: Collectible items and pickup logic
- **EnemyAI.cs**: Enemy behavior and AI patterns
- **LevelManager.cs**: Level progression and management

## 🎯 Features

✅ **AI-Powered Enhancements**: Get creative suggestions for your game idea
✅ **Unity Code Generation**: Complete C# scripts ready for Unity
✅ **Project Structure**: Proper Unity folder organization
✅ **Multiple Genres**: Platformer, RPG, Puzzle, Shooter, and more
✅ **Beginner-Friendly**: Simple web interface with Streamlit
✅ **Extensible**: Easy to add new templates and features

## 📚 Documentation

- **[SETUP.md](SETUP.md)**: Detailed setup and troubleshooting guide
- **[Backend API](http://localhost:8000/docs)**: Interactive API documentation
- **[Health Check](http://localhost:8000/health)**: Backend status

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new game genres and templates
- Improve the AI prompts and suggestions
- Enhance the UI and user experience
- Add more Unity script templates
- Implement asset generation features

## 🔧 Troubleshooting

Having issues? Check out:
1. **[SETUP.md](SETUP.md)** - Comprehensive setup guide
2. **`python test_setup.py`** - Verify your installation
3. **Backend logs** - Check for error messages
4. **API documentation** - Test endpoints directly

## 📝 License

MIT License - feel free to use and modify!

---

**🎉 Ready to create your first AI-generated Unity game? Follow the setup guide and start building!** 
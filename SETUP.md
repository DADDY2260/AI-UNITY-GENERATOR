# 🚀 Setup Guide - AI Unity Game Generator

This guide will help you set up and run the AI Unity Game Generator from scratch. Follow these steps carefully!

## 📋 Prerequisites

Before you start, make sure you have:

- **Python 3.8 or higher** installed
- **Git** installed (optional, for version control)
- **Unity 2020.3 or later** (for testing generated projects)
- **OpenAI API key** (get one from [OpenAI Platform](https://platform.openai.com/api-keys))

## 🛠️ Installation Steps

### Step 1: Clone or Download the Project

If you have Git:
```bash
git clone <your-repo-url>
cd ai-unity-generator
```

If you don't have Git, download the project files and extract them to a folder.

### Step 2: Install Python Dependencies

Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

**Troubleshooting:**
- If you get permission errors, try: `pip install --user -r requirements.txt`
- On Windows, you might need: `python -m pip install -r requirements.txt`
- If you have multiple Python versions, use: `python3 -m pip install -r requirements.txt`

### Step 3: Set Up Environment Variables

1. **Copy the example environment file:**
   ```bash
   # On Windows:
   copy env.example .env
   
   # On Mac/Linux:
   cp env.example .env
   ```

2. **Edit the .env file** and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

   **Important:** Replace `your_actual_api_key_here` with your real OpenAI API key!

### Step 4: Test the Installation

Run this command to check if everything is installed correctly:
```bash
python -c "import fastapi, streamlit, openai; print('✅ All dependencies installed successfully!')"
```

## 🚀 Running the Application

### Option 1: Using the Startup Scripts (Recommended)

1. **Start the Backend:**
   ```bash
   python start_backend.py
   ```
   You should see:
   ```
   🚀 Starting AI Unity Game Generator Backend...
   📡 Server will be available at: http://localhost:8000
   ```

2. **Open a new terminal and start the Frontend:**
   ```bash
   python start_frontend.py
   ```
   You should see:
   ```
   🎮 Starting AI Unity Game Generator Frontend...
   ✅ Backend is running!
   🌐 Frontend will be available at: http://localhost:8501
   ```

3. **Open your web browser** and go to: `http://localhost:8501`

### Option 2: Manual Startup

1. **Start Backend (Terminal 1):**
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. **Start Frontend (Terminal 2):**
   ```bash
   cd frontend
   streamlit run app.py
   ```

## 🎮 Using the Application

1. **Describe your game idea** in the text area
2. **Select a genre** (optional, but helpful)
3. **Click "Enhance My Idea"** to get AI suggestions
4. **Review and select enhancements** you want to include
5. **Generate your Unity project** and download it!

## 🔧 Troubleshooting

### Common Issues:

**❌ "OPENAI_API_KEY environment variable is not set"**
- Make sure you created a `.env` file with your API key
- Check that the `.env` file is in the project root directory
- Verify there are no spaces around the `=` sign

**❌ "Backend server is not running"**
- Make sure you started the backend first
- Check that port 8000 is not being used by another application
- Try running `python start_backend.py` again

**❌ "Module not found" errors**
- Make sure you installed all dependencies: `pip install -r requirements.txt`
- Check that you're using Python 3.8 or higher
- Try creating a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

**❌ "Connection refused" errors**
- Make sure both backend and frontend are running
- Check that the ports (8000 and 8501) are not blocked by firewall
- Try restarting both servers

### Getting Help:

1. **Check the logs** in the terminal for error messages
2. **Verify your OpenAI API key** is valid and has credits
3. **Test the API directly** by visiting `http://localhost:8000/docs`
4. **Check the health endpoint** at `http://localhost:8000/health`

## 📁 Project Structure

```
ai-unity-generator/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # Main server
│   │   ├── llm/            # AI integration
│   │   ├── generators/     # Code generation
│   │   └── templates/      # Unity templates
├── frontend/               # Streamlit frontend
│   └── app.py
├── requirements.txt        # Python dependencies
├── start_backend.py       # Backend startup script
├── start_frontend.py      # Frontend startup script
├── env.example            # Environment template
└── README.md              # Project documentation
```

## 🎯 Next Steps

Once you have the application running:

1. **Test with a simple game idea** like "2D platformer with a jumping character"
2. **Explore the generated Unity project** structure
3. **Customize the templates** in `backend/app/templates/`
4. **Add new game genres** by modifying the prompts
5. **Deploy to a cloud platform** like Heroku or Render

## 🆘 Still Having Issues?

If you're still having problems:

1. **Check your Python version:** `python --version`
2. **Verify all files are present** in the project directory
3. **Try running in a clean virtual environment**
4. **Check if your firewall is blocking the ports**
5. **Make sure you have an active internet connection** (for OpenAI API)

## 🎉 Success!

Once everything is working, you should be able to:
- ✅ Enter a game idea and get AI enhancements
- ✅ Select which enhancements to include
- ✅ Generate a complete Unity project
- ✅ Download and import the project into Unity

Happy game development! 🎮 
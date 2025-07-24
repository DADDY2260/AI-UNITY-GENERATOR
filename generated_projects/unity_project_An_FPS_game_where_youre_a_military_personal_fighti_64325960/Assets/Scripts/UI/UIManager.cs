using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// UIManager - Handles UI elements and interactions
/// Generated for: An FPS game where youre a military personal fighting a war
/// </summary>
public class UIManager : MonoBehaviour
{
    [Header("UI Panels")]
    public GameObject mainMenuPanel;
    public GameObject gameplayPanel;
    public GameObject pausePanel;
    public GameObject gameOverPanel;
    public GameObject settingsPanel;
    
    [Header("Gameplay UI")]
    public Text scoreText;
    public Text levelText;
    public Text timerText;
    
    
    [Header("Menu UI")]
    public Button startButton;
    public Button settingsButton;
    public Button quitButton;
    public Button resumeButton;
    public Button restartButton;
    public Button mainMenuButton;
    
    [Header("Settings")]
    public Slider musicSlider;
    public Slider sfxSlider;
    public Toggle fullscreenToggle;
    
    // Private variables
    private GameManager gameManager;
    private float gameTimer = 0f;
    private bool isTimerRunning = false;
    
    void Start()
    {
        gameManager = GameManager.Instance;
        
        // Setup button listeners
        SetupButtonListeners();
        
        // Setup settings
        SetupSettings();
        
        // Subscribe to events
        if (gameManager != null)
        {
            gameManager.OnScoreChanged += UpdateScore;
            gameManager.OnGameOver += ShowGameOver;
            
        }
        
        // Show main menu initially
        ShowMainMenu();
    }
    
    void Update()
    {
        // Update timer
        if (isTimerRunning)
        {
            gameTimer += Time.deltaTime;
            UpdateTimer();
        }
    }
    
    void SetupButtonListeners()
    {
        if (startButton != null)
            startButton.onClick.AddListener(StartGame);
        
        if (settingsButton != null)
            settingsButton.onClick.AddListener(ShowSettings);
        
        if (quitButton != null)
            quitButton.onClick.AddListener(QuitGame);
        
        if (resumeButton != null)
            resumeButton.onClick.AddListener(ResumeGame);
        
        if (restartButton != null)
            restartButton.onClick.AddListener(RestartGame);
        
        if (mainMenuButton != null)
            mainMenuButton.onClick.AddListener(ShowMainMenu);
    }
    
    void SetupSettings()
    {
        if (musicSlider != null)
        {
            musicSlider.value = PlayerPrefs.GetFloat("MusicVolume", 0.5f);
            musicSlider.onValueChanged.AddListener(SetMusicVolume);
        }
        
        if (sfxSlider != null)
        {
            sfxSlider.value = PlayerPrefs.GetFloat("SFXVolume", 0.5f);
            sfxSlider.onValueChanged.AddListener(SetSFXVolume);
        }
        
        if (fullscreenToggle != null)
        {
            fullscreenToggle.isOn = Screen.fullScreen;
            fullscreenToggle.onValueChanged.AddListener(SetFullscreen);
        }
    }
    
    public void ShowMainMenu()
    {
        HideAllPanels();
        if (mainMenuPanel != null) mainMenuPanel.SetActive(true);
        
        // Stop timer
        isTimerRunning = false;
        gameTimer = 0f;
    }
    
    public void StartGame()
    {
        HideAllPanels();
        if (gameplayPanel != null) gameplayPanel.SetActive(true);
        
        // Start timer
        isTimerRunning = true;
        gameTimer = 0f;
        
        // Initialize UI
        UpdateScore(0);
        UpdateTimer();
        
    }
    
    public void ShowSettings()
    {
        HideAllPanels();
        if (settingsPanel != null) settingsPanel.SetActive(true);
    }
    
    public void ResumeGame()
    {
        if (gameManager != null)
        {
            gameManager.TogglePause();
        }
    }
    
    public void RestartGame()
    {
        if (gameManager != null)
        {
            gameManager.RestartGame();
        }
    }
    
    public void QuitGame()
    {
        if (gameManager != null)
        {
            gameManager.QuitGame();
        }
    }
    
    void ShowGameOver()
    {
        HideAllPanels();
        if (gameOverPanel != null) gameOverPanel.SetActive(true);
        
        // Stop timer
        isTimerRunning = false;
    }
    
    void HideAllPanels()
    {
        if (mainMenuPanel != null) mainMenuPanel.SetActive(false);
        if (gameplayPanel != null) gameplayPanel.SetActive(false);
        if (pausePanel != null) pausePanel.SetActive(false);
        if (gameOverPanel != null) gameOverPanel.SetActive(false);
        if (settingsPanel != null) settingsPanel.SetActive(false);
    }
    
    void UpdateScore(int score)
    {
        if (scoreText != null)
        {
            scoreText.text = $"Score: {score}";
        }
    }
    
    
    
    void UpdateTimer()
    {
        if (timerText != null)
        {
            int minutes = Mathf.FloorToInt(gameTimer / 60f);
            int seconds = Mathf.FloorToInt(gameTimer % 60f);
            timerText.text = string.Format("{0:00}:{1:00}", minutes, seconds);
        }
    }
    
    
    
    // Settings methods
    void SetMusicVolume(float volume)
    {
        PlayerPrefs.SetFloat("MusicVolume", volume);
        // Apply to audio manager if you have one
        // AudioManager.Instance.SetMusicVolume(volume);
    }
    
    void SetSFXVolume(float volume)
    {
        PlayerPrefs.SetFloat("SFXVolume", volume);
        // Apply to audio manager if you have one
        // AudioManager.Instance.SetSFXVolume(volume);
    }
    
    void SetFullscreen(bool isFullscreen)
    {
        Screen.fullScreen = isFullscreen;
    }
    
    void OnDestroy()
    {
        // Unsubscribe from events
        if (gameManager != null)
        {
            gameManager.OnScoreChanged -= UpdateScore;
            gameManager.OnGameOver -= ShowGameOver;
            
        }
    }
} 
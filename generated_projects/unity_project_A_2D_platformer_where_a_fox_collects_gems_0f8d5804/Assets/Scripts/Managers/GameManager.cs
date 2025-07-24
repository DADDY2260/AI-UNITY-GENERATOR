using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// GameManager - Manages game state and flow
/// Generated for: A 2D platformer where a fox collects gems
/// </summary>
public class GameManager : MonoBehaviour
{
    // Singleton pattern
    public static GameManager Instance { get; private set; }
    
    [Header("Game Settings")]
    public int targetScore = 1000;
    
    
    [Header("UI References")]
    public GameObject gameOverPanel;
    public GameObject pausePanel;
    public UnityEngine.UI.Text scoreText;
    public UnityEngine.UI.Text levelText;
    
    // Game state
    private int currentScore = 0;
    private bool isGamePaused = false;
    private bool isGameOver = false;
    
    // Events
    public System.Action<int> OnScoreChanged;
    public System.Action OnGameOver;
    public System.Action OnLevelComplete;
    
    void Awake()
    {
        // Singleton pattern
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    void Start()
    {
        InitializeGame();
    }
    
    void Update()
    {
        // Handle pause input
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            TogglePause();
        }
        
        // Handle restart input
        if (Input.GetKeyDown(KeyCode.R))
        {
            RestartGame();
        }
    }
    
    void InitializeGame()
    {
        currentScore = 0;
        isGameOver = false;
        isGamePaused = false;
        
        // Hide UI panels
        if (gameOverPanel != null) gameOverPanel.SetActive(false);
        if (pausePanel != null) pausePanel.SetActive(false);
        
        // Update UI
        UpdateUI();
        
        // Resume time
        Time.timeScale = 1f;
    }
    
    public void AddScore(int points)
    {
        currentScore += points;
        OnScoreChanged?.Invoke(currentScore);
        UpdateUI();
        
        // Check for win condition
        if (currentScore >= targetScore)
        {
            
            GameOver(true);
            
        }
    }
    
    
    
    public void GameOver(bool isWin = false)
    {
        if (isGameOver) return;
        
        isGameOver = true;
        OnGameOver?.Invoke();
        
        // Show game over UI
        if (gameOverPanel != null)
        {
            gameOverPanel.SetActive(true);
            
            // Update game over text
            UnityEngine.UI.Text gameOverText = gameOverPanel.GetComponentInChildren<UnityEngine.UI.Text>();
            if (gameOverText != null)
            {
                gameOverText.text = isWin ? "You Win!" : "Game Over";
            }
        }
        
        // Pause the game
        Time.timeScale = 0f;
    }
    
    public void TogglePause()
    {
        if (isGameOver) return;
        
        isGamePaused = !isGamePaused;
        
        if (isGamePaused)
        {
            Time.timeScale = 0f;
            if (pausePanel != null) pausePanel.SetActive(true);
        }
        else
        {
            Time.timeScale = 1f;
            if (pausePanel != null) pausePanel.SetActive(false);
        }
    }
    
    public void RestartGame()
    {
        
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
    
    public void QuitGame()
    {
        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #else
        Application.Quit();
        #endif
    }
    
    void UpdateUI()
    {
        if (scoreText != null)
        {
            scoreText.text = $"Score: {currentScore}";
        }
        
        
    }
    
    // Public getters
    public int GetCurrentScore() => currentScore;
    public bool IsGamePaused() => isGamePaused;
    public bool IsGameOver() => isGameOver;
    
} 
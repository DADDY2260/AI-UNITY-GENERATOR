using UnityEngine;

/// <summary>
/// PlayerController - Handles player movement and input
/// Generated for: A 2d platformer where a queen has to fight demons who possess her empire
/// </summary>
public class PlayerController : MonoBehaviour
{
    [Header("Movement Settings")]
    public float moveSpeed = 5f;
    public float jumpForce = 10f;
    
    
    [Header("Ground Check")]
    public Transform groundCheck;
    public float groundCheckRadius = 0.2f;
    public LayerMask groundLayer = 1;
    
    // Private variables
    private Rigidbody2D rb;
    private bool isGrounded;
    
    private float horizontalInput;
    
    // Animation (if you have an Animator)
    private Animator animator;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        animator = GetComponent<Animator>();
        
        
        // Create ground check if not assigned
        if (groundCheck == null)
        {
            GameObject check = new GameObject("GroundCheck");
            check.transform.SetParent(transform);
            check.transform.localPosition = new Vector3(0, -0.5f, 0);
            groundCheck = check.transform;
        }
    }
    
    void Update()
    {
        // Get input
        horizontalInput = Input.GetAxisRaw("Horizontal");
        
        // Check if grounded
        isGrounded = Physics2D.OverlapCircle(groundCheck.position, groundCheckRadius, groundLayer);
        
        
        
        // Jump input
        if (Input.GetButtonDown("Jump"))
        {
            
            if (isGrounded)
            {
                Jump(jumpForce);
            }
            
        }
        
        // Update animations
        UpdateAnimations();
    }
    
    void FixedUpdate()
    {
        // Move horizontally
        Move();
    }
    
    void Move()
    {
        Vector2 velocity = rb.velocity;
        velocity.x = horizontalInput * moveSpeed;
        rb.velocity = velocity;
        
        // Flip sprite based on direction
        if (horizontalInput != 0)
        {
            transform.localScale = new Vector3(
                Mathf.Sign(horizontalInput), 
                1, 
                1
            );
        }
    }
    
    void Jump(float force)
    {
        rb.velocity = new Vector2(rb.velocity.x, force);
        
        // Play jump sound if you have one
        // AudioManager.Instance.PlaySound("jump");
    }
    
    void UpdateAnimations()
    {
        if (animator != null)
        {
            // Set animation parameters
            animator.SetFloat("Speed", Mathf.Abs(horizontalInput));
            animator.SetBool("IsGrounded", isGrounded);
            
        }
    }
    
    // Visualize ground check in editor
    void OnDrawGizmosSelected()
    {
        if (groundCheck != null)
        {
            Gizmos.color = isGrounded ? Color.green : Color.red;
            Gizmos.DrawWireSphere(groundCheck.position, groundCheckRadius);
        }
    }
    
    
} 
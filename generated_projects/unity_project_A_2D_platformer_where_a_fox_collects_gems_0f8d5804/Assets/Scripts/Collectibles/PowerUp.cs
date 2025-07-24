using UnityEngine;

/// <summary>
/// PowerUp - Handles collectible power-up behavior
/// Generated for: A 2D platformer where a fox collects gems
/// </summary>
public class PowerUp : MonoBehaviour
{
    public enum PowerUpType { Speed, Jump, Shield, Health, Custom }
    public PowerUpType type = PowerUpType.Speed;
    public float duration = 5f;
    public int value = 1;
    public GameObject collectEffect;
    public AudioClip collectSound;
    public bool destroyOnCollect = true;

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            ApplyPowerUp(other.gameObject);
            if (collectEffect != null)
                Instantiate(collectEffect, transform.position, Quaternion.identity);
            if (collectSound != null)
                AudioSource.PlayClipAtPoint(collectSound, transform.position);
            if (destroyOnCollect)
                Destroy(gameObject);
            else
                gameObject.SetActive(false);
        }
    }

    void ApplyPowerUp(GameObject player)
    {
        PlayerController pc = player.GetComponent<PlayerController>();
        if (pc != null)
        {
            switch (type)
            {
                case PowerUpType.Speed:
                    pc.StartCoroutine(pc.TemporarySpeedBoost(duration, value));
                    break;
                case PowerUpType.Jump:
                    pc.StartCoroutine(pc.TemporaryJumpBoost(duration, value));
                    break;
                case PowerUpType.Shield:
                    pc.ActivateShield(duration);
                    break;
                case PowerUpType.Health:
                    pc.AddHealth(value);
                    break;
                case PowerUpType.Custom:
                    // Custom logic here
                    break;
            }
        }
    }
} 
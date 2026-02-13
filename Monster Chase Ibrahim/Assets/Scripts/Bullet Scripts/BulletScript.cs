using System;
using UnityEngine;

public class BulletScript : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created

    public float speed;
    private Rigidbody2D myBody;
    private const string ENEMY_TAG = "Enemy";
    public static event Action onDestroyBullet;
    void Start()
    {
        myBody = GetComponent<Rigidbody2D>();
        
    }

    // Update is called once per frame
    void Update()
    {
        myBody.linearVelocity = new Vector2(speed,myBody.linearVelocity.y);
    }
    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.collider.CompareTag(ENEMY_TAG))
        {
            Destroy(collision.collider.gameObject);
            onDestroyBullet?.Invoke();
            Destroy(gameObject);
        }
    }
   
}

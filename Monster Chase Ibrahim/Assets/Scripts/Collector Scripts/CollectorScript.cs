using UnityEngine;

public class CollectorScript : MonoBehaviour
{
    private const string ENEMY_TAG = "Enemy";
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.collider.CompareTag(ENEMY_TAG))
        {
            Debug.Log("Enter in if");
            Destroy(collision.collider.gameObject);

        }
        else
        {
            Debug.Log("Enter in else");
            
        }
    }
}

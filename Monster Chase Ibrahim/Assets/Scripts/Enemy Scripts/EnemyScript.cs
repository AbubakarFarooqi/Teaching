using UnityEngine;

public class EnemyScript : MonoBehaviour
{
    private Rigidbody2D myBody;
    private const string BULLET_TAG = "bullet";
    public float speed; // will chaange it to public
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        myBody = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        myBody.linearVelocity = new Vector2(speed,myBody.linearVelocity.y);
    }
    
}

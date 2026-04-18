using TMPro;
using UnityEngine;

public class ScoreScript : MonoBehaviour
{
    public TextMeshProUGUI scoreText;
    public  static int score = 0;
    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        scoreText.text = $"Score: {score}";
        BulletScript.onDestroyBullet += AddInScore;
    }

    // Update is called once per frame
    void Update()
    {
        scoreText.text = $"Score: {score}";
    }
    void AddInScore()
    {
        score++;
    }
    void OnDestroy()
    {
        BulletScript.onDestroyBullet -= AddInScore;
    }

}

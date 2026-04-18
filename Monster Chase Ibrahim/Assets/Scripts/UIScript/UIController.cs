using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;
public class UIController : MonoBehaviour
{
    public TextMeshProUGUI scoreText;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        scoreText.text = "Scores: " + ScoreScript.score.ToString();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void ReplayGame()
    {
        Live_Script.lives = 3;
        SceneManager.LoadScene("SampleScene");
    }
}

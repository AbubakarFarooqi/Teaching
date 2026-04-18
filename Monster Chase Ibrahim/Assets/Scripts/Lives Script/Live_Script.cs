using UnityEngine;
using TMPro;
using UnityEngine;
using System;

public class Live_Script : MonoBehaviour
{
      public static int lives = 3;
    public TextMeshProUGUI life_text;
    public static event Action IfLives0;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        life_text.text = $"lives: {lives}";
        PlayerScript.onPlayerCollidesWithEnemy += Decreaselifes;
    }


    // Update is called once per frame
    void Update()
    {
        life_text.text = $"lives: {lives}";
    }
    void Decreaselifes()
    {
        lives--;
        if (lives <= 0)
        {
            IfLives0?.Invoke();
        }
    }
    void OnDestroy()
    {
        PlayerScript.onPlayerCollidesWithEnemy -= Decreaselifes;    
    }
}

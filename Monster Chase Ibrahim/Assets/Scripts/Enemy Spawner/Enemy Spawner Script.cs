using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemySpawnerScript : MonoBehaviour
{
    private string[] positions = {"Left","Right"};
    [SerializeField]
    private List<GameObject> enemies;
    [SerializeField]
    private Transform leftPos;
    [SerializeField]
    private Transform rightPos;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        StartCoroutine(SpawnEnemy());
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    IEnumerator SpawnEnemy()
    {
        while (true)
        {
            yield return new WaitForSeconds(Random.Range(1,3));
            int idx = Random.Range(0,enemies.Count);
            string position = positions[Random.Range(0,2)]; 
            var spawnEnemy = Instantiate(enemies[idx]);
            if (position == "Left")
            {
                spawnEnemy.transform.position = leftPos.position;
                spawnEnemy.GetComponent<EnemyScript>().speed = Random.Range(3,10);
                spawnEnemy.GetComponent<SpriteRenderer>().flipX = false;
            }
            else
            {
                spawnEnemy.transform.position = rightPos.position;
                spawnEnemy.GetComponent<EnemyScript>().speed = Random.Range(3,10) * -1;
                spawnEnemy.GetComponent<SpriteRenderer>().flipX = true;

            }
        }
    }
}

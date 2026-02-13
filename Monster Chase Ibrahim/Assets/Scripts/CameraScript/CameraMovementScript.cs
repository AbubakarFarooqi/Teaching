using UnityEngine;

public class CameraMovementScript : MonoBehaviour
{
    private float maxX;
    private float minX;
    private Transform playerTransform;
    private Vector3 tempCamPosition;
    


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        playerTransform = GameObject.FindGameObjectWithTag("Player").transform;
        minX = -22f;
        maxX = 22f;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void LateUpdate()
    {
        if (playerTransform.position.x > minX && playerTransform.position.x < maxX)// player x is in range of min and max value only then i will execute the following 3 lines
        {
            tempCamPosition = transform.position;
            tempCamPosition.x = playerTransform.position.x;
            transform.position = tempCamPosition;
        }
        
    }
}

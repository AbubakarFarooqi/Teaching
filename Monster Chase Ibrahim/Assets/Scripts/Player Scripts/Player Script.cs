using System;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.SceneManagement;
public class PlayerScript : MonoBehaviour // inheritance
{
    // it means this variable can be used outside this class
    [SerializeField] // attribute
    private float motionForce;
    [SerializeField]
    private float jumpForce;
    private float moveDir = 0;
    private bool isGrounded = true;
    private const string WALK_ANIMATION = "Walk";
    private const string JUMP_ANIMATION = "Jump";
    private Transform transform;
    private Rigidbody2D myBody;
    private SpriteRenderer spriteRenderer;
    private Animator animator;
    private const string ENEMY_TAG = "Enemy";
    private bool isBulletOnScreen;

    [SerializeField]
    private GameObject BulletReference;
    public static event Action onPlayerCollidesWithEnemy;


    void Awake()
    {
        BulletScript.onDestroyBullet += HandleDestroyBullet;
    }
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        transform = GetComponent<Transform>();
        animator = GetComponent<Animator>();
        myBody = GetComponent<Rigidbody2D>();
        spriteRenderer = GetComponent<SpriteRenderer>();
        isBulletOnScreen = false;
        Live_Script.IfLives0 += endLife;

    }

    // Update is called once per frame
    void Update()
    {
        WalkPlayer();
        WalkAnimation();
        PlayerJump();
        animator.SetBool(JUMP_ANIMATION,!isGrounded);
        ShootBullet();
    }

    void WalkPlayer()
    {
        
        if (Keyboard.current.aKey.isPressed)
        {
            moveDir = -1f;
            transform.position += new Vector3(moveDir,0,0) * motionForce * Time.deltaTime;
            spriteRenderer.flipX = true;

        }
        else if (Keyboard.current.dKey.isPressed)
        {
            moveDir = 1f;
            transform.position += new Vector3(moveDir,0,0) * motionForce * Time.deltaTime;
            spriteRenderer.flipX = false;

        }
        else
        {
            moveDir = 0;
        }

    }
     void endLife()
    {
       SceneManager.LoadScene("GameOverScene"); 
    }
    void WalkAnimation()
    {
        if (moveDir != 0)
        {
            animator.SetBool(WALK_ANIMATION,true);
        }
        else
        {
            animator.SetBool(WALK_ANIMATION,false);
        }

    }
    void PlayerJump()
    {
        if (Keyboard.current.spaceKey.isPressed && isGrounded)
        {
            isGrounded = false;
            myBody.AddForce(new Vector2(0f,jumpForce),ForceMode2D.Impulse);
        }
    }
    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.collider.CompareTag("Ground"))
        {
            isGrounded = true;
        }
          if (collision.collider.CompareTag(ENEMY_TAG))
        {
            Debug.Log("inside if");
            onPlayerCollidesWithEnemy?.Invoke();
            this.transform.position = new Vector2(-0.03f, -1.98f);
        }
    }

    // void ShootBullet()
    // {
    //     if ( !isBulletOnScreen && Mouse.current.leftButton.IsPressed())
    //     {
            
    //        isBulletOnScreen = true;

    //        if (spriteRenderer.flipX == true)
    //         {
    //             var bullet = Instantiate(BulletReference);
    //             bullet.transform.position = new Vector2(this.GetComponent<CapsuleCollider2D>().bounds.center.x
    //             +
    //             this.GetComponent<CapsuleCollider2D>().bounds.extents.x-0.5f,
    //             this.GetComponent<CapsuleCollider2D>().bounds.center.y
    //             );
    //             bullet.GetComponent<BulletScript>().speed = -10;
    //             bullet.GetComponent<SpriteRenderer>().flipX = true;
    //         }
    //         else
    //         {
    //             var bullet = Instantiate(BulletReference);
    //             bullet.transform.position = new Vector2(this.GetComponent<CapsuleCollider2D>().bounds.center.x
    //             +
    //             this.GetComponent<CapsuleCollider2D>().bounds.extents.x+0.5f,
    //             this.GetComponent<CapsuleCollider2D>().bounds.center.y
    //             );
    //             bullet.GetComponent<BulletScript>().speed = -10;
    //             bullet.GetComponent<SpriteRenderer>().flipX = true;
    //             bullet.GetComponent<BulletScript>().speed = 10;
    //             bullet.GetComponent<SpriteRenderer>().flipX = false;
    //         }
    //     }
    // }

    void ShootBullet()
    {
        if (!isBulletOnScreen && Mouse.current.leftButton.IsPressed())
        {
            var bullet = Instantiate(BulletReference);



            isBulletOnScreen = true;
            if (spriteRenderer.flipX == true)
            {
                bullet.transform.position = new Vector2(this.GetComponent<CapsuleCollider2D>().bounds.center.x + this.GetComponent<CapsuleCollider2D>().bounds.extents.x + -0.5f, this.GetComponent<CapsuleCollider2D>().bounds.center.y);
                bullet.GetComponent<BulletScript>().speed = -10;
                bullet.GetComponent<SpriteRenderer>().flipX = true;
            }
            else
            {
                bullet.transform.position = new Vector2(this.GetComponent<CapsuleCollider2D>().bounds.center.x + this.GetComponent<CapsuleCollider2D>().bounds.extents.x + 2f, this.GetComponent<CapsuleCollider2D>().bounds.center.y);
                bullet.GetComponent<BulletScript>().speed = 10;
                bullet.GetComponent<SpriteRenderer>().flipX = false;
            }

        }
    }
    void HandleDestroyBullet()
    {
        isBulletOnScreen = false;
    }
}








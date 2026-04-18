import './Card.css'
// import b747 from './assets/747.png'
//import a380 from './assets/a380.png'

function Card(props) {
  

  return (
    <>
    <div class="card">
      <div class="b747-2">
        <div class="img">
          <img src={props.image} alt="" />
        </div>
      </div>
      
      <div className="content">
      <h1>{props.header}</h1>
      <p>{props.description}</p>
        <button class="button">press to see the 747s</button>

      
      </div>
      
      

    </div>

    </>
  )
}

export default Card
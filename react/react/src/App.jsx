import {useState} from 'react'
import './App.css'
import TabButton from './TabButton/TabButton.jsx'
import { EXAMPLES } from './data.js'

function App() {
  
  const [content,setContent] = useState()



  const HandleSelect = (type) =>{
    if (type == 'components')
      setContent('components')
    else if (type == 'jsx')
      setContent('jsx')
    else if (type == 'state')
      setContent('state')
    else if (type == 'props')
      setContent('props')
  }
  return (
    <>
    <div className='main'>
      <div class="buttons">
      <TabButton isSelected ={content === 'components'} onSelect={()=>HandleSelect('components')}>Components</TabButton>
      <TabButton isSelected ={content === 'jsx'} onSelect={()=>HandleSelect('jsx')}>JSX</TabButton>
      <TabButton isSelected ={content === 'state'} onSelect={()=>HandleSelect('state')}>State</TabButton>
      <TabButton isSelected ={content === 'props'} onSelect={()=>HandleSelect('props')}>Props</TabButton>
     </div>
     {content ? <div className='content-area'>
      <h3>{EXAMPLES[content].title}</h3>
      <p>{EXAMPLES[content].description} </p>
      <pre>
        <code>
          {EXAMPLES[content].code}
        </code>
      </pre>
     </div> : <p>Please Select a button</p>}
    </div>
    </>
  )
}


export default App
















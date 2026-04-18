import './TabButton.css'

function TabButton({children,onSelect,isSelected}) {
  

  return (
    <>
    <button className= {`abc ${isSelected ? 'active' : ''}`} onClick={onSelect}>{children}</button>
    </>
  )
}

export default TabButton
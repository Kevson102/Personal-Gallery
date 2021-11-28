console.log("hello kevson")

const copyButtons = [...document.getElementsByClassName('copy-btn')]
console.log(copyButtons)

// let previous = null

copyButtons.forEach(btn => btn.addEventListener('click', ()=>{
  console.log('click')
  const link = btn.getAttribute('image-link')
  console.log(link)
  navigator.clipboard.writeText(link)
  btn.textContent = 'image link copied...'

  // navigator.clipboard.readText().then

  // if (previous){
  //   previous.textContent = 'Copy Image Link'
  // }
  // previous=btn
}))
let audio = new Audio('../music/Netflix.mp3')
let btnEnviar = document.querySelector('#enviar')

btnEnviar.addEventListener('click', () => {
    audio.play()
 })
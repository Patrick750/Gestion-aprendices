const fondos = document.querySelectorAll(".fondos")
let index = 0
function Mostrar(){

    fondos.forEach(imgs => {
        imgs.classList.remove("active")
    })
    fondos[index].classList.add("active")
}

function Pasar(){
    index++
    if(index >= fondos.length){
        index = 0
    }
    Mostrar()
}
setInterval(Pasar, 6000)
Mostrar()


const nombre = document.getElementById('nombre');
const apellido = document.getElementById('apellido');   
const correo = document.getElementById('correo');
const telefono = document.getElementById('contraseña');
const documento = document.getElementById('documento');
const error = document.getElementById('error');
const btn = document.getElementById('btn');

function validarCorreo(event) {
    if([nombre.value, apellido.value, correo.value, telefono.value, documento.value].includes('')){
        error.innerText = 'Todos los campos son obligatorios';
    }else{
        error.innerText = '';
    }

}   
btn.addEventListener('click', validarCorreo);


   
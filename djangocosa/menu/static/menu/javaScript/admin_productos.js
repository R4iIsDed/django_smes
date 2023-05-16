var codigo_prod = document.getElementById("codigo");
var nombre_prod = document.getElementById("nombre");
var descripcion_prod = document.getElementById("descripcion");
var precio_prod = document.getElementById("precio");
var imagen_prod = document.getElementById("imagen");

const form1 = document.getElementById("form");
var msj = document.getElementById("warnings");

form1.addEventListener("submit", e =>{
    e.preventDefault();
    let msjmostrar = "";
    let entrar = false;

    if(nombre_prod.value.length < 4 || nombre_prod.value.length > 10){
        msjmostrar = msjmostrar + 'El nombre debe tener entre 4 y 10 caracteres';
        entrar = true;
    }
   else{
    msj.innerHTML = "Enviado";
    }
}
);
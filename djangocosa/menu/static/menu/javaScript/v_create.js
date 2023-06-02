$(document).ready(function(e){
    
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#create").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            Rut: {
                required:true,
                minlength: 5,
                noSpace: true
            },
            name: {
                required:true,
                minlength: 5,
                noSpace: true
            },
            apellido: {
                required:true,
                minlength: 5,
                noSpace: true
            },
            telefono: {
                required:true,
                minlength: 5,
                noSpace: true
            },
            email: { 
                required: true,
                email: true,
                noSpace: true
            },
            password: {
                required: true,
                minlength: 5,
                noSpace: true
            },
            password2: {
                required: true,
                equalTo: "#password"
            },
            address: {
                required: true,
                minlength: 8
            },
            securityanswer: {
                required: true,
                minlength: 2,
                noSpace: true
            }
        },
        messages: {
            name:{
                required: " Ingrese su nombre ",
                minlength: " El nombre debe tener minimo 5 caracteres "
            },
            email: {
                required: " Ingrese su email ",
                email: " Ingrese un email real con el formato de ejemplo@ejemplo.com "
            },
            password: {
                required: " Ingrese la nueva contraseña",
                minlength: " La contraseña debe contener al menos 5 caracteres "
            },
            password2: {
                required: " Porfavor repita la nueva contraseña ",
                equalTo: " Las contraseñas no coinciden "
            },
            address: {
                required: " Ingrese su direccion ",
                minlength: " La direccion debe tener minimo 8 caracteres "
            },
            securityanswer: {
                required: " Ingrese la respuesta a su pregunta de seguridad ",
                minlength: " La respuesta debe contener mas de 2 caracteres  "
            }
        }
    })
    e.preventdefault();
})







jQuery.extend(jQuery.validator.messages, {
    required: " Seleccione una opcion. "
});
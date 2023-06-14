$(document).ready(function(e){
    
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#login").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            email: { 
                required: true,
                email: true,
                noSpace: true
            },
            password: {
                required: true,
                minlength: 5,
                noSpace: true
            }
        },
        messages: {
            email: {
                required: " Ingrese su email ",
                email: " Ingrese un email real con el formato de ejemplo@ejemplo.com "
            },
            password: {
                required: " Ingrese su contraseña ",
                minlength: " La contraseña debe contener al menos 5 caracteres "
            }
        }
    })
})
$(document).ready(function(e){
    
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#forgoh").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            email: { 
                required: true,
                email: true,
            },
            securityanswer: {
                required: true,
                minlength: 2,
                noSpace: true
            },
            newpassword: {
                required: true,
                minlength: 5,
                noSpace: true
            },
            confirmpassword: {
                required: true,
                equalTo: "#newpassword"
            }

        },
        messages: {
            email: {
                required: " Ingrese su email ",
                email: " Ingrese un email real con el formato de ejemplo@ejemplo.com "
            },
            securityanswer: {
                required: " Ingrese la respuesta a su pregunta de seguridad ",
                minlength: " La respuesta debe contener mas de 2 caracteres "
            },
            newpassword: {
                required: " Ingrese la nueva contraseña ",
                minlength: " La contraseña debe contener al menos 5 caracteres "
            },
            confirmpassword: {
                required: " Porfavor repita la nueva contraseña ",
                equalTo: " Las contraseñas no coinciden "
            }
        }
    })
    e.preventdefault();
})







jQuery.extend(jQuery.validator.messages, {
    required: " Seleccione una opcion. "
});
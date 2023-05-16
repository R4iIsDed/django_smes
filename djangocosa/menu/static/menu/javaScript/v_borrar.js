$(document).ready(function(e){
    
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#erase").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            password: {
                required: true,
                minlength: 5,
                noSpace: true
            }
        },
        messages: {
            password: {
                required: " Ingrese su contraseña ",
                minlength: " La contraseña debe contener al menos 5 caracteres "
            }
        }
    })
    e.preventdefault();
})
$(document).ready(function(e){
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
      jQuery.validator.addMethod("notEqual", function(value, element, param) {
        return this.optional(element) || value != $(param).val();
       }, " La nueva contraseña no puede ser la anterior");
    $("#change").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            currentpassword: {
                required: true,
                minlength: 5,
                noSpace: true
            },
            newpassword: {
                required: true,
                minlength: 5,
                noSpace: true,
                notEqual: "#currentpassword"
            },
            confirmpassword: {
                required: true,
                equalTo: "#newpassword"
            }

        },
        messages: {
            currentpassword: {
                required: " Ingrese su contraseña actual ",
                minlength: " La respuesta debe contener mas de 5 caracteres "
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
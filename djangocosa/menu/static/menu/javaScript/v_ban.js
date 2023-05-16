$(document).ready(function(e){
    
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#wea").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            weon: {
                required: true,
                minlength: 5,
                noSpace: true
            }
        },
        messages: {
            weon: {
                required: " Ingrese motivo ",
                minlength: " El motivo debe contener al menos 5 caracteres "
            }
        }
    }),
    $("#wea3").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            weon3: {
                required: true,
                minlength: 5,
                noSpace: true
            }
        },
        messages: {
            weon3: {
                required: " Ingrese motivo ",
                minlength: " El motivo debe contener al menos 5 caracteres "
            }
        }
    })
    e.preventdefault();
})
$(document).ready(function(e){
    
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
      $("#wea2").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            weon2: {
                required: true,
                minlength: 5,
                noSpace: true
            }
        },
        messages: {
            weon2: {
                required: " Ingrese motivo ",
                minlength: " El motivo debe contener al menos 5 caracteres "
            }
        }
    }),
    $("#buscar").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            search: {
                required: true,
                minlength: 5,
                noSpace: true
            }
        },
        messages: {
            search: {
                required: " Ingrese persona a buscar ",
                minlength: " El nombre debe contener al menos 5 caracteres "
            }
        }
    })
    e.preventdefault();
})
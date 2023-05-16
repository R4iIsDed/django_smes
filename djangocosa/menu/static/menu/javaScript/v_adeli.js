$(document).ready(function(e){
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#form").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            codigo: {
                required: true,
                minlength: 6,
                noSpace: true
            }
        },messages: {
            codigo: {
                required: "ingrese el codigo producto",
                minlength: "el codigo producto debe tener minimo 6 caracteres",
            }
        }
    })
});
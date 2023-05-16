$(document).ready(function(e){
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#compra").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            cardNumber: {
                required: true,
                number: true,
                minlength: 13,
                maxlength: 18,
                noSpace: true
            },
            ccv: {
                required: true,
                number: true,
                min:100,
                max:999,
                noSpace: true
            },
            nameOnCard: {
                required: true,
                minlength: 10,
                maxlength: 30,
            },
        },
        messages: {
            cardNumber: {
                required: " Ingrese su numero de tarjeta de credito / debito ",
                number: " El numero de tarjeta contiene caracteres ",
                minlength: " El numero debe contener un largo minimo de 13 ",
                maxlength: " El numero debe contener maximo 18 caracteres ",
            },
            ccv: {
                required: " Ingrese el ccv de la tarjeta (numeros en la parte trasera) ",
                number: " El ccv solo contiene numeros ",
                min: " El ccv tiene un largo de 3 numeros ",
                max: " El ccv tiene un largo de 3 numeros "
            },
            nameOnCard: {
                required: " Ingrese nombre que se encuentre en la tarjeta ",
                minlength: " El nombre deber tener minimo 10 caracteres ",
                maxlength: " El nombre debe contener maximo 30 caracteres "
            }
        }
    })
    });













    
jQuery.extend(jQuery.validator.messages, {
    required: "Seleccione una opcion."
});
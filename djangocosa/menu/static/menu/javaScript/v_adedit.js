$(document).ready(function(e){
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $("#formulario-edicion").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            codigo: {
                minlength: 6,
                noSpace: true
            },
            nombre: {
                minlength: 6,
                noSpace: true
            },
            descripcion: {
                minlength: 10,
                maxlength: 200,
                noSpace: true
            },
            precio: {
                number: true,
                noSpace: true,
                min: 1
            }
        },
        messages: {
            codigo: {
                minlength: "el codigo producto debe tener minimo 6 caracteres"
            },
            nombre: {
                minlength: "el nombre debe contar con al menos 6 caracteres",
                noSpace: "reemplaze los espacios con - porfavor"
            },
            descripcion: {
                minlength: "la descripcion debe contar con al menos 10 caracteres",
                maxlength: "la descripcion tiene un maximo posible de 200 caracteres",
                noSpace: "reemplaze los espacios con - porfavor"
            },
            precio: {
                number: "ingrese un precio correto (solo se admiten numeros)",
                min: "los numeros negativos no son permitidos"
            }
        }
    })
    });

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
            },
            nombre: {
                required: true,
                minlength: 6,
                noSpace: true
            },
            descripcion: {
                required: true,
                minlength: 10,
                maxlength: 200,
                noSpace: true
            },
            precio: {
                required: true,
                number: true,
                noSpace: true,
                min: 1
            }
        },
        messages: {
            codigo: {
                required: "ingrese el codigo producto",
                minlength: "el codigo producto debe tener minimo 6 caracteres",
            },
            nombre: {
                required: "ingrese nombre prodcuto",
                minlength: "el nombre debe contar con al menos 6 caracteres",
                noSpace: "reemplaze los espacios con - porfavor"
            },
            descripcion: {
                required: "ingrese descripcion prodcuto",
                minlength: "la descripcion debe contar con al menos 10 caracteres",
                maxlength: "la descripcion tiene un maximo posible de 200 caracteres",
                noSpace: "reemplaze los espacios con - porfavor"
            },
            precio: {
                required: "ingrese precio del producto",
                number: "ingrese un precio correto (solo se admiten numeros)",
                min: "los numeros negativos no son permitidos"
            }
        }
    })
    });













    
jQuery.extend(jQuery.validator.messages, {
    required: "Seleccione una imagen"
});
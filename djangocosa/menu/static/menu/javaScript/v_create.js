$(document).ready(function(e){
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
      }, "No dejes espacios por favor");
    $.validator.addMethod('lowercasesymbols', function(value) {
    return value.match(/^[a-z\[!@# $%&*\/?=_.,:;\\\]"-]+$/);
    }, 'La contraseña debe contener solo caracteres minisculas y al menos un simbolo');
    $("#create").validate({
        errorClass: "error fail-alert",

        validClass: "valid success-alert",

        rules: {
            Rut: {
                required:true,
                minlength: 5,
                noSpace: true,
                maxlenght: 20,
            },
            name: {
                required:true,
                minlength: 5,
                noSpace: true
            },
            apellido: {
                required:true,
                minlength: 5,
                noSpace: true
            },
            telefono: {
                required:true,
                minlength: 5,
                noSpace: true
            },
            email: { 
                required: true,
                email: true,
                noSpace: true
            },
            password: {
                required: true,
                minlength: 5,
                noSpace: true,
                maxlenght:20,
                lowercasesymbols: true
            },
            password2: {
                required: true,
                equalTo: "#password"
            },
            securityanswer: {
                required: true,
                minlength: 2,
                noSpace: true
            }
        },
        messages: {
            Rut:{
                required: " Ingrese su Rut ",
                minlength: " El Rut debe tener 10 caracteres minimo ",
                maxlenght: "el rut debe tener maximo 20 caracteres"
            },
            name:{
                required: " Ingrese su nombre ",
                minlength: " El nombre debe tener minimo 5 caracteres "
            },
            apellido:{
                required: " Ingrese su apellido ",
                minlength: " El nombre debe tener minimo 5 caracteres "
            },
            telefono: {
                required: "debe ingresar un numero de telefono",
                minlength: "el numero de telefono debe tener al menos 5 caracteres"
            },
            email: {
                required: " Ingrese su email ",
                email: " Ingrese un email real con el formato de ejemplo@ejemplo.com "
            },
            password: {
                required: " Ingrese la nueva contraseña",
                minlength: " La contraseña debe contener al menos 5 caracteres "
            },
            password2: {
                required: " Porfavor repita la nueva contraseña ",
                equalTo: " Las contraseñas no coinciden "
            },
            securityanswer: {
                required: " Ingrese la respuesta a su pregunta de seguridad ",
                minlength: " La respuesta debe contener mas de 2 caracteres  "
            }
        }
    })
})







jQuery.extend(jQuery.validator.messages, {
    required: " Seleccione una opcion. "
});
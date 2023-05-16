
let url = "https://apis.digital.gob.cl/fl/feriados"
$.get(url, function(respuesta) {

    let feriado = respuesta[respuesta.length -14]

    $("#feriado").text("Proximo feriado " + feriado.nombre + "-" + feriado.fecha)

},"json")
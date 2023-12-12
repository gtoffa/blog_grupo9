function resaltarTexto() {
  // Obtener el valor del campo de búsqueda
  var buscarTexto = document.getElementById("buscarInput").value.trim().toLowerCase();

  if (buscarTexto.length > 0) {
    // Obtener todos los elementos <p>
    var textos = document.querySelectorAll("p,h2");

    // Iterar sobre los elementos y cambiar el color si coinciden
    textos.forEach(function (texto) {
      var contenidoOriginal = texto.textContent;
      var contenidoLower = contenidoOriginal.toLowerCase();

      // Limpiar resaltados previos
      texto.innerHTML = contenidoOriginal;

      // Encontrar las coincidencias y resaltarlas
      var inicioCoincidencia = contenidoLower.indexOf(buscarTexto);
      while (inicioCoincidencia !== -1) {
        var finCoincidencia = inicioCoincidencia + buscarTexto.length;
        var parteResaltada = contenidoOriginal.slice(
          inicioCoincidencia,
          finCoincidencia
        );

        // Reemplazar la coincidencia con el texto resaltado
        texto.innerHTML = texto.innerHTML.replace(
          parteResaltada,
          '<strong style="color: #007bff;margin-left: 0px">' +
            parteResaltada +
            "</strong>"
        );

        // Encontrar la próxima coincidencia
        inicioCoincidencia = contenidoLower.indexOf(
          buscarTexto,
          finCoincidencia
        );
      }
    });
  }
}


$(document).ready(function() {
  $('.treeview').mdbTreeview();
});
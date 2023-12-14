function resaltarTexto() {
  // Obtener el valor del campo de búsqueda
  var buscarTexto = document
    .getElementById("buscarInput")
    .value.trim()
    .toLowerCase();

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

function alerta(titulo, icon, text) {
  //para icon puede ser: warning, success, error, info

  $.toast({
    text: text, // Text that is to be shown in the toast
    heading: titulo, // Optional heading to be shown on the toast
    icon: icon, // Type of toast icon
    showHideTransition: "slide", // fade, slide or plain
    allowToastClose: true, // Boolean value true or false
    hideAfter: 3000, // false to make it sticky or number representing the miliseconds as time after which toast needs to be hidden
    stack: 5, // false if there should be only one toast at a time or a number representing the maximum number of toasts to be shown at a time
    position: "bottom-right", // bottom-left or bottom-right or bottom-center or top-left or top-right or top-center or mid-center or an object representing the left, right, top, bottom values

    textAlign: "left", // Text alignment i.e. left, right or center
    loader: true, // Whether to show loader or not. True by default
    loaderBg: "#9EC600", // Background color of the toast loader
    beforeShow: function () {}, // will be triggered before the toast is shown
    afterShown: function () {}, // will be triggered after the toat has been shown
    beforeHide: function () {}, // will be triggered before the toast gets hidden
    afterHidden: function () {}, // will be triggered after the toast has been hidden
  });
}

function setearFuncionClick() {
  $(".confirmDelete").on("click", function () {
    var idcomment = $(this).data("idcomment");

    $("#confirmDeleteBtn").data("idcomment", idcomment);
    //$("#confirmDeleteBtn").attr("idcomment", idcomment)
  });

  $(".editComment").on("click", function () {
    var idComentario = $(this).data("idcomment");

    var formularioClonado = $("#formulario-comentario").clone();

    // Modificar atributos según necesidades
    formularioClonado.attr("id", "formulario-comentario" + idComentario);
    formularioClonado
      .find("#commenTextArea")
      .val($("#sub-heading-" + idComentario).text());
    formularioClonado
      .find("#commenTextArea")
      .attr("id", "commenTextArea" + idComentario);
    formularioClonado
      .find("#enviar-comentario")
      .attr("onclick", "enviarComentario(" + idComentario + ")");
    formularioClonado
      .find("#enviar-comentario")
      .attr("id", "enviar-comentario" + idComentario);

    formularioClonado
      .find("#comentario-error")
      .attr("id", "comentario-error" + idComentario);

    formularioClonado.find("#loading").attr("id", "loading" + idComentario);

    formularioClonado.find("#loading").attr("id", "loading" + idComentario);

    // Agregar el formulario clonado al contenedor
    $("#comment" + idComentario).html(formularioClonado);
  });
}

function enviarComentario(id_comentario) {
  var comentario_contenido = $("#commenTextArea" + id_comentario).val();

  if (!comentario_contenido) {
    $("#comentario-error" + id_comentario).text("El comentario es obligatorio");
    return;
  } else {
    $("#comentario-error" + id_comentario).text("");
  }

  var noticia_id = parseInt($("#page_content").attr("idNoticia"));
  // Mostrar indicador de carga
  $("#loading" + id_comentario).removeClass("d-none");
  var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  $("#commenTextArea" + id_comentario).attr("disabled", true);
  $("#enviar-comentario" + id_comentario).prop("disabled", true);
  $.ajax({
    type: "POST",
    url: "ajax/cargar_comentarios/" + noticia_id + "/",
    data: {
      contenido: comentario_contenido,
      id_comentario: id_comentario,
      csrfmiddlewaretoken: csrf_token, // Reemplaza esto con la lógica para obtener el token CSRF
    },
    dataType: "json",
    success: function (data) {
      // Actualizar el contenido del div con ID "test" con la respuesta del servidor
      $("#test").html(data.content);
      setearFuncionClick();
      alerta("Informacion", "info", "Tu comentario se ha publicado");
      $("#commenTextArea" + id_comentario).attr("disabled", false);
      $("#enviar-comentario" + id_comentario).prop("disabled", false);

      // Limpiar el textarea y ocultar el indicador de carga
      $("#commenTextArea" + id_comentario).val("");
      $("#loading" + id_comentario).addClass("d-none");
    },
    error: function (xhr, status, error) {
      console.error(xhr.responseText);
      alerta("Error", "warning", "Error: Tu comentario no se ha publicado");
      $("#commenTextArea" + id_comentario).attr("disabled", false);
      $("#enviar-comentario" + id_comentario).prop("disabled", false);
    },
  });
}

$(document).ready(function () {
  setearFuncionClick();

  //Crear Comentarios
  $("#enviar-comentario").click(function () {
    enviarComentario("");
  });

  //Eliminar comentarios
  $("#confirmDeleteBtn").on("click", function () {
    var idcomment = $(this).data("idcomment");

    $("#loading-comment").removeClass("d-none");

    var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $(".btncomment").prop("disabled", true);
    $.ajax({
      type: "GET",
      url: "ajax/eliminar_comentarios/" + idcomment + "/",
      data: { csrfmiddlewaretoken: csrf_token },
      dataType: "json",
      success: function (data) {
        // Actualizar el contenido del div con ID "test" con la respuesta del servidor
        $("#test").html(data.content);
        setearFuncionClick();
        alerta("Informacion", "info", "Tu comentario se ha eliminado");

        $(".btncomment").prop("disabled", false);

        $("#loading-comment").addClass("d-none");
        $("#confirmModal").modal("hide");
      },
      error: function (xhr, status, error) {
        console.error(xhr.responseText);
        alerta("Error", "warning", "Error: Tu comentario no se ha eliminado");

        $(".btncomment").prop("disabled", false);
        $("#loading-comment").addClass("d-none");
      },
    });
  });

  $("#confirmModal").on("show.bs.modal", function (event) {
    var button = $(event.relatedTarget);
    var idcomment = button.data("idcomment");
    $(this)
      .find(".modal-body")
      .text("¿Estás seguro de que deseas eliminar el comentario?");
  });
});

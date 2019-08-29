$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-preguntaUno .modal-content").html("");
        $("#modal-preguntaUno").modal("show");
        console.log("ingreso al primer metodo")
      },
      success: function (data) {
        $("#modal-preguntaUno .modal-content").html(data.html_form);
         console.log("ingreso al segundo metodo")
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list);
          $("#modal-preguntaUno").modal("hide");
           console.log("ingreso al tercero metodo")
        }
        else {
          $("#modal-preguntaUno .modal-content").html(data.html_form);
           console.log("ingreso al cuarto metodo")
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-modulo-uno").click(loadForm);
  $("#modal-preguntaUno").on("submit", ".js-modulo-uno-form", saveForm);

  // // Update book
  // $("#book-table").on("click", ".js-update-book", loadForm);
  // $("#modal-book").on("submit", ".js-book-update-form", saveForm);
  //
  // // Delete book
  // $("#book-table").on("click", ".js-delete-book", loadForm);
  // $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});
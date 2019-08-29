$(function () {

  /* Functions */
  setTimeout(function () {
  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        console.log("Ingreso a la primera Funcion");
        $("#modal-book .modal-content").html("");
        console.log("Ingreso a la segunda Funcion");
        $("#modal-book").modal("show").trigger('click');
        console.log("Ingreso a la tercera Funcion");
      },
      success: function (data) {
        console.log("Ingreso a la cuarta Funcion");
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  };
   }, 5000);

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          console.log("Ingreso a la quinta Funcion");
          $("#book-table tbody").html(data.html_book_list);
          console.log("Ingreso a la sexta Funcion");
          $("#modal-book").modal("hide");
        }
        else {
          console.log("Ingreso a la primera Funcion");
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-book").click(loadForm);
  $("#modal-book").on("submit", ".js-book-create-form", saveForm);

  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
  $("#modal-book").on("submit", ".js-book-update-form", saveForm);

  // Delete book
  $("#book-table").on("click", ".js-delete-book", loadForm);
  $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});

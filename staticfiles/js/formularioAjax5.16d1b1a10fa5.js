$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-book .modal-content").html("");
                $("#modal-book").modal({backdrop: 'static', keyboard: false});
            },
            success: function (data) {
                $("#modal-book .modal-content").html(data.html_formCUATRO);
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
                    $("#modal-book").modal("hide");
                } else {
                    $("#modal-book .modal-content").html(data.html_formCUATRO);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book

     setTimeout(function () {
        $(".js-create-bookCUATRO").click(loadForm).trigger('click');
         console.log("******* Creando la pregunta 9 **************");
    }, 300000);


    $("#modal-book").on("submit", ".js-book-create-formCUATRO", saveForm);
     console.log("******* Guardando la pregunta 9 **************");


    //
    // // Update book
    // $("#book-table").on("click", ".js-update-book", loadForm);
    // $("#modal-book").on("submit", ".js-book-update-form", saveForm);
    //
    // // Delete book
    // $("#book-table").on("click", ".js-delete-book", loadForm);
    // $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});

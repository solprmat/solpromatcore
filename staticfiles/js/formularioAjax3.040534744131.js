$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                console.log("************  10 * ****************");
                $("#modal-book .modal-content").html("");
               console.log("************  11 * ****************");
                $("#modal-book").modal("show");
                console.log("************  12 * ****************");
            },
            success: function (data) {
                console.log("************  13 * ****************");
                $("#modal-book .modal-content").html(data.html_formDOS);
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
                    console.log("************  14 * ****************");
                    $("#book-table tbody").html(data.html_book_list);
                    console.log("************  15 * ****************");
                    $("#modal-book").modal("hide");
                } else {
                    console.log("************  16 * ****************");
                    $("#modal-book .modal-content").html(data.html_formDOS);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book

     setTimeout(function () {
        $(".js-create-bookDOS").click(loadForm).trigger('click');
        console.log("************  17 * ****************");
        $("#botonGuardarPreguntaUno").prop('disabled', false);
        console.log("************  18 * ****************");
    }, 70000);


    $("#modal-book").on("submit", ".js-book-create-formDOS", saveForm);
    console.log("************  19 * ****************");












    // Update book
    $("#book-table").on("click", ".js-update-book", loadForm);
    $("#modal-book").on("submit", ".js-book-update-form", saveForm);

    // Delete book
    $("#book-table").on("click", ".js-delete-book", loadForm);
    $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});
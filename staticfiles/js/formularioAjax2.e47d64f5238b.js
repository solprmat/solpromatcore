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
                $("#modal-book2 .modal-content2").html("");
               console.log("************  11 * ****************");
                $("#modal-book2").modal("show");
                console.log("************  12 * ****************");
            },
            success: function (data) {
                console.log("************  13 * ****************");
                $("#modal-book2 .modal-content2").html(data.html_formUNO);
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
                    $("#modal-book2").modal("hide");
                } else {
                    console.log("************  16 * ****************");
                    $("#modal-book2 .modal-content2").html(data.html_formUNO);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book

     setTimeout(function () {
        $(".js-create-bookUNO").click(loadForm).trigger('click');
        console.log("************  17 * ****************");
        $("#botonGuardarPreguntaUno").prop('disabled', false);
        console.log("************  18 * ****************");
    }, 28000);


    $("#modal-book").on("submit", ".js-book-create-formUNO", saveForm);
    console.log("************  19 * ****************");












    // Update book
    $("#book-table").on("click", ".js-update-book", loadForm);
    $("#modal-book").on("submit", ".js-book-update-form", saveForm);

    // Delete book
    $("#book-table").on("click", ".js-delete-book", loadForm);
    $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});

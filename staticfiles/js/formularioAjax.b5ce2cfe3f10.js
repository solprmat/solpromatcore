$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                console.log(" ************  1 * **************** ");
                $("#modal-book .modal-content").html("");
                console.log("************  2 * ****************");
                $("#modal-book").modal("show");
                $.blockUI({ message: $('#modal-book') });
                console.log("************  3 * ****************");
            },
            success: function (data) {
                console.log("************  4 * ****************");
                $("#modal-book .modal-content").html(data.html_form);
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
                    console.log("************  5 * ****************");
                    $("#book-table tbody").html(data.html_book_list);
                    console.log("Ingreso a la sexta Funcion");
                    $("#modal-book").modal("hide");
                } else {
                    console.log("************  6 * ****************");
                    $("#modal-book .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book

    setTimeout(function () {
        $(".js-create-book").click(loadForm).trigger('click');
        console.log("************  7 * ****************");

    }, 20000);


    $("#modal-book").on("submit", ".js-book-create-form", saveForm);
    console.log("************  9 * ****************");




    // Update book
    $("#book-table").on("click", ".js-update-book", loadForm);
    $("#modal-book").on("submit", ".js-book-update-form", saveForm);

    // Delete book
    $("#book-table").on("click", ".js-delete-book", loadForm);
    $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});

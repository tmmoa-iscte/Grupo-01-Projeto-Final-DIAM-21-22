$(document).ready(function() {
    // Confirmação de se o utilizador quer apagar uma Thread.
    $("#delete-thread-button").click(function() {
        return confirm("Tem a certeza de que pretende apagar a thread?");
    });

    // Confirmação de se o administrador quer apagar uma Categoria.
    $("#delete-category-form").submit(function() {
        return confirm("Tem a certeza de que pretende apagar a categoria?");
    });

    // Confirmação de se o administrador quer apagar uma secção.
    $("#delete-section-button").click(function() {
        return confirm("Tem a certeza de que pretende apagar a secção?");
    });

    // Confirmação de se o utilizador quer apagar um comentário.
    $(".delete-comment-button").click(function() {
        return confirm("Tem a certeza de que pretende apagar o comentário?");
    });
});
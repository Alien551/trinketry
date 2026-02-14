// Скрипт, переданный в конструкции document.ready может быть исполнен
// только после того, как страница сайта загрузится
$(document).ready(function () {
    // обработка события нажатия на элемент с классом "add-to-cart"
    $(document).on("click", ".add-to-cart", function (event) {
        event.preventDefault(); // блокирует базовое действие
        var product_id = $(this).data('product-id');
        var add_to_cart_url = $(this).attr("href");

        $.ajax({
            dataType: "json",
            type: "POST",
            url: add_to_cart_url,
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response) {
                // alert('Товар успешно добавлен в корзину!');
            },
            error: function(xhr, status, error) {
                console.error(error);
                alert('Возникла проблема с удалением товара.');
            }
        });
    });
    $(document).on("click", ".remove-from-cart", function (event) {
        event.preventDefault(); // блокирует базовое действие

        var CartCounter = $("#cart-items-counter");
        var cartCount = parseInt(CartCounter.text() || 0);

        var product_id = $(this).data('product-id');
        var remove_from_cart_url = $(this).attr("href");

        $.ajax({
            dataType: "json",
            type: "POST",
            url: remove_from_cart_url,
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response) {
                // alert('Товар удалён');
                var cartContainer = $("#cart_container");
                cartContainer.html(response.order_html)
            },
            error: function(xhr, status, error) {
                console.error(error);
                alert('Возникла проблема с добавлением товара.');
            }
        });
    });
});
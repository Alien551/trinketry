from .models import Order, OrderProducts

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user

        order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
        order_products = OrderProducts.objects.filter(order=order)
    else:
        order = "заглушка для гостевой корзины"
        order_products = "заглушка для товаров гостевой корзины"
    return {"order_products":order_products, "order":order}

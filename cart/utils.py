from .models import Order, OrderProducts

def get_order(request):
    if request.user.is_authenticated:
        order, _ = Order.objects.get_or_create(
            user=request.user,
            is_complete=False)

    else:
        if not request.session.session_key:
            request.session.create()
        order, _ = Order.objects.get_or_create(
            session_key=request.session.session_key,
            is_complete=False)

    return order

def get_order_products(request):
    order = get_order(request)
    order_products = OrderProducts.objects.filter(order=order)
    return order_products

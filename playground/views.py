
from django.shortcuts import render
from django.db.models import Q, F, Func, Value, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Customer, OrderItem, Product
from tags.models import TaggedItem

def say_hello(request):
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # products = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )
    # customers = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' -  '), 'last_name')
    # )
    # customer_orders = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name'),
    #     orders=Count('order'),
    # ).order_by('full_name')
    query_set = Product.objects.all()
    list(query_set)
    query_set[0]
    return render(
        request, 'hello.html', {'name': 'Jino', 'query_set': query_set})

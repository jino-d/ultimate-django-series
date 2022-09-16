from django.contrib import admin
from .models import Promotion
from .models import Collection
from .models import Product
from .models import Customer
from .models import Order
from .models import OrderItem
from .models import Address
from .models import Cart
from .models import CartItem


admin.site.register(Promotion)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)

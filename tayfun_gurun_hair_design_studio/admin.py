from django.contrib import admin

from .models import Order,Service,Customer

# Register your models here.
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(Customer)

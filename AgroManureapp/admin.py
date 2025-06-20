from django.contrib import admin
from .models import products,Order_details

# Register your models here.
class productsAdmin(admin.ModelAdmin):
  pass
admin.site.register(products,productsAdmin)
admin.site.register(Order_details)

from django.contrib import admin
from pages.models import Order,Contact

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=("Addres","phone_number")
    list_filter=("coffee_type",)
    
class ContactAdmin(admin.ModelAdmin):
    list_display=('email',"number")

admin.site.register(Order,OrderAdmin)

admin.site.register(Contact,ContactAdmin)


from django.contrib import admin
from accounts.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display="__all__"

admin.site.register(User)
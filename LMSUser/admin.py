from django.contrib import admin
from .models import CustomUser
# Register your models here.

# admin.site.register(CustomUser)


@admin.register(CustomUser)
class CustomUserView(admin.ModelAdmin):
    list_display = ("Username", "Name")

    def Username(self, obj):
        return obj.user.username

    def Name(self, obj):
        return obj.user.first_name+" "+obj.user.last_name

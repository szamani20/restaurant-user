from django.contrib import admin

from .models import Member, Order

admin.site.register(Order)
admin.site.register(Member)

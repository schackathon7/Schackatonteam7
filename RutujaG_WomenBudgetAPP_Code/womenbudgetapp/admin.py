from django.contrib import admin
from .models import Customer, GoalSet, Wallet


admin.site.site_header = "Women Budget APP"

# Register your models here.

admin.site.register(Customer)
admin.site.register(GoalSet)
admin.site.register(Wallet)

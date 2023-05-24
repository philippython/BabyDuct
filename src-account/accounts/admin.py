from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(BuyerShipmentAddress)
admin.site.register(BuyerPaymentInformation)
admin.site.register(SellerProfile)
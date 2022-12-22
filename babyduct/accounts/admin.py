from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ConsumerProfile, ProducerProfile

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ConsumerProfile)
admin.site.register(ProducerProfile)
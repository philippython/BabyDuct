from django.contrib import admin
from .models import User, ConsumerProfile, ProducerProfile

# Register your models here.
admin.site.register(User)
admin.site.register(ConsumerProfile)
admin.site.register(ProducerProfile)
from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Advisor)
admin.site.register(Booking)
admin.site.register(User)
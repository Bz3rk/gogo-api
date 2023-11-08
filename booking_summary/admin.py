from django.contrib import admin
from .models import BookingSummary, Junction, Ride, PriceTable

# Register your models here.

admin.site.register(BookingSummary)
admin.site.register(Junction)
admin.site.register(Ride)
admin.site.register(PriceTable)

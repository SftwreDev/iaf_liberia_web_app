from django.contrib import admin

# Register your models here.
from .models import ContactUsInquiries, BookAnEstimate


admin.site.register(ContactUsInquiries)
admin.site.register(BookAnEstimate)


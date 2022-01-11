from django.contrib import admin
from  django.contrib.auth.models  import  Group  # new

# Register your models here.
from .models import ContactUsInquiries, BookAnEstimate


admin.site.register(ContactUsInquiries)
admin.site.register(BookAnEstimate)

admin.site.site_header  =  "International Aluminum Factory"  
admin.site.site_title  =  "International Aluminum Factory | Admin Page"
admin.site.index_title  =  "International Aluminum Factory | Admin Page"

admin.site.unregister(Group)  # new
from django.db import models


# Create your models here.


class ContactUsInquiries(models.Model):
    """
        Database Model Table for Contact Us Inquiries
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name} | {self.email}"


class BookAnEstimate(models.Model):
    """
        Database Model Table for Book an Estimate
    """
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    schedule = models.DateField(auto_now_add=False, null=True, blank=True)
    existing = models.CharField(max_length=255)
    how_do_you_hear = models.CharField(max_length=255)
    referral_name = models.CharField(max_length=255)
    comments = models.TextField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Customer Name : {self.last_name}, {self.first_name} | Schedule :  {self.schedule}"
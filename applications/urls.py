from django.urls import path

from .views.homepage.homepage_views import *
from .views.estimate.book_an_estimate_views import *
from .views.products.products_views import *
from .views.contact_us.contact_us_views import *
from .views.about_us.about_us_views import *
from .views.admin.admin_views import *

app_name = "applications"

urlpatterns = [
    path("", homepage, name="homepage"),
    path("book-an-estimate", book_an_estimate, name="book_an_estimate"),
    path("products", product_page, name="product_page"),
    path("contact-us", contact_us_page, name="contact_us_page"),
    path("about-us", about_us_page, name="about_us_page"),
    path("admin", admin_page, name="admin_page"),

    
    path("app/v1/contact/contact-us/send-email", send_email, name="send_email"),
    path("app/v1/book-an-estimate", save_estimate, name="save_estimate"),
]

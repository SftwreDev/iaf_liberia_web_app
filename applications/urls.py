from django.urls import path

from .views.homepage.homepage_views import *
from .views.estimate.book_an_estimate_views import *
from .views.products.products_views import *
from .views.contact_us.contact_us_views import *

app_name = "applications"

urlpatterns = [
    path("", homepage, name="homepage"),
    path("app/v1/estimate/book-an-estimate", book_an_estimate, name="book_an_estimate"),
    path("app/v1/products/products-page", product_page, name="product_page"),
    path("app/v1/contact/contact-us", contact_us_page, name="contact_us_page"),
]

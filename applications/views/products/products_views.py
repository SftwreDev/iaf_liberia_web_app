from django.shortcuts import render



def product_page(request):
    """
        Function for Product page
    """
    # Declare HTML Template
    template_name = "products/product_page.html"
    context = {
        "product_status" : "active",
    }

    # Return render response
    return render(request, template_name, context)
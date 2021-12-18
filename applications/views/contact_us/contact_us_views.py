from django.shortcuts import render


def contact_us_page(request):
    """
        Functions for Contact Us Page
    """
    # Declare HTML Template
    template_name = "contact/contact_us.html"

    context = {
        "contact_status" : "active",
    }

    # Return render response
    return render(request, template_name, context)
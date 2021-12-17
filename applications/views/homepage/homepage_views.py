from django.shortcuts import render


def homepage(request):
    """
        This functions handles the homepage
    """

    # Declare html template
    template_name = "homepage/homepage.html"

    #  Set context variables
    context = {
        "homepage_status" : "active"
    }

    # Return render response
    return render(request, template_name, context)

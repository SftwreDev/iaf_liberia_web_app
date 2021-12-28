from django.shortcuts import render



def about_us_page(request):
    """
        Function for About us page
    """
    # Declare HTML template
    template_name = "about_us/about_us.html"

    #Declare context variables
    context = {
        "about_status" : "active",
    }

    # Return render response
    return render(request, template_name, context)
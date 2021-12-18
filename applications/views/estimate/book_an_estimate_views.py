from django.shortcuts import render



def book_an_estimate(request):
    """
        Function for Book An Estimate Page
    """
    # Declare HTML Template
    template_name = "estimate/book_an_estimate.html"

     # Return render response
    return render(request, template_name)
from django.shortcuts import render, redirect


from applications.models import BookAnEstimate

def book_an_estimate(request):
    """
        Function for Book An Estimate Page
    """
    # Declare HTML Template
    template_name = "estimate/book_an_estimate.html"
    service1 = {
        "ALUMINUM WINDOWS",
        "ALUMINUM DOORS",
        "KITCHEN CABINETS",
        "HANDRAILS",
        "WINDOW BLINDS",
        "SIGNBOARDS",
    }
    service2 = {
        "CEILINGS",
        "STEEL DOORS",
        "STEEL RAILS",
        "PARTITIONING",
        "ROOFING ZINC",
    }

    existing_customer = {
        "Yes", "No"
    }
    context = {
        "service1": service1,
        "service2": service2,
        "existing_customer" : existing_customer
    }
    # Return render response
    return render(request, template_name, context)



def save_estimate(request):
    """
        Function for saving estimate inquiries
    """
    if request.method == 'POST':
        last_name = request.POST['lastName']
        first_name = request.POST['firstName']
        location = request.POST['location']
        contact = request.POST['contact']
        email = request.POST['email']
        # if request.POST['service1']:
        #     service1 = request.POST['service1']
        # if request.POST['service2']:
        #     service2 = request.POST['service2']
        existing = request.POST['existing']
        how_do_you_hear = request.POST['howDoYouHear']
        ref_name = request.POST['refName']
        comments = request.POST['comments']

        saveEstimate = BookAnEstimate.objects.create(
            last_name=last_name, first_name=first_name,
            location=location, contact=contact,
            email=email, existing=existing, how_do_you_hear=how_do_you_hear,
            referral_name=ref_name, comments=comments,
        )

        return redirect('applications:book_an_estimate')
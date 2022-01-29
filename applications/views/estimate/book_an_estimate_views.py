from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from applications.models import BookAnEstimate, Service

def book_an_estimate(request):
    """
        Function for Book An Estimate Page
    """
    # Declare HTML Template
    template_name = "estimate/book_an_estimate.html"
    service1 = [1, 2, 3, 4, 5, 6]
    service2 = [7, 8, 9, 10, 11]

    existing_customer = {
        "Yes", "No"
    }

    service1 = Service.objects.filter(id__in=service1)
    service2 = Service.objects.filter(id__in=service2)

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
        service = request.POST.getlist('service')
        existing = request.POST['existing']
        how_do_you_hear = request.POST['howDoYouHear']
        ref_name = request.POST['refName']
        comments = request.POST['comments']
        schedule = request.POST['date']
        try:
            saveEstimate = BookAnEstimate.objects.create(
                last_name=last_name, first_name=first_name,
                location=location, contact=contact,
                email=email, existing=existing, how_do_you_hear=how_do_you_hear,
                referral_name=ref_name, comments=comments,
                schedule=schedule
            )

            for id in service:
                saveEstimate.service.add(id)
        except:
            pass
            
        # Send email confirmation
        email_template = "application/email.html"
        subject = "International Aluminum Factory"
        html_message = """
            <!doctype html>
            <html lang="en">
                <head>
                    <!-- Required meta tags -->
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">

                    <title>IAF Liberia</title>

                </head>
                <body style="background-color: #ffffff; font-family: 'Arial', cursive; scroll-behavior: smooth; ">
                    <div>
                        <p style="color: #1d2d75; font-size: 60px; text-align: center;">International Aluminum Factory</p>
                        <p style="text-align: center; font-size: 24px;">Providing solutions for global problems</p>
                        <br>
                        <div style="margin: 50px 100px 100px 100px;">
                            <p style="align-items: center; font-size: 18px;">
                                Good Day! <br>
                                <br>

                                Thank you for booking a schedule for estimation<br>
                                Here's your schedule detail : <br>
                                <br>
                                <table id="customers" style="font-family: Arial, Helvetica, sans-serif; border-collapse: collapse; width: 100%;">
                                <tr>
                                    <th style="border: 1px solid #ddd; padding: 8px; padding-top: 12px; padding-bottom: 12px; text-align: left background-color: #1d2d75; color: white;">Customer Name</th>
                                    <th style="border: 1px solid #ddd; padding: 8px; padding-top: 12px; padding-bottom: 12px; text-align: left background-color: #1d2d75; color: white;">Location</th>
                                    <th style="border: 1px solid #ddd; padding: 8px; padding-top: 12px; padding-bottom: 12px; text-align: left background-color: #1d2d75; color: white;">Services</th>
                                    <th style="border: 1px solid #ddd; padding: 8px; padding-top: 12px; padding-bottom: 12px; text-align: left background-color: #1d2d75; color: white;">Schedule</th>
                                </tr>
                            
                                <tr>
                                    <td style="border: 1px solid #ddd; padding: 8px;">{last_name}, {first_name}</td>
                                    <td style="border: 1px solid #ddd; padding: 8px;">{location}</td>
                                    <td style="border: 1px solid #ddd; padding: 8px;">{schedule}</td>
                                </tr>
                                </table>
                                <br>
                                Thank You and have a great day!

                            </p>
                        </div>
                    </div>
                </body>
            </html>	
        """.format(last_name=last_name, first_name=first_name, location=location, schedule=schedule)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        email_message = EmailMultiAlternatives(
            subject, html_message, email_from, recipient_list,)
        email_message.attach_alternative(html_message, "text/html")
        email_message.send()

        admin_message = f"""
            A client sent an inquiry!
            Name : {last_name}
            Email : {email_from}
            Contact : {contact}
            Message : {comments}
        """
        inform_admin = EmailMultiAlternatives("CodeHub | Admin", admin_message, email_from, ['garcia.giancarlo714@gmail.com', ])
        inform_admin.send()
        return redirect('applications:book_an_estimate')
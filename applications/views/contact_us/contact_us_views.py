from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

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

def send_email(request):
    """
        Functions for sending email
    """
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']

        # create_object = Inquiries.objects.create(
        #     full_name=full_name, email=email,
        #     contact=contact, message=message
        # )

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
                <div style=" text-align: center;">
                    <p style="color: #1d2d75; font-size: 60px; align-items: center;">International Aluminum Factory</p>
                    <p style="align-items: center; font-size: 24px;">Providing solutions for global problems</p>
                    <br>
                    <p style="align-items: center; font-size: 24px;">
                        Hi {full_name}, <br>
                        <br>

                        Thank you for reaching International Aluminum Factory. <br>
                        Please wait for our reply to cater your inquiries. <br>
                        <br>
                        <br>

                        Thank You and have a great day!

                    </p>
                </div>
            </body>
        </html>	
        """.format(full_name=full_name)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        email_message = EmailMultiAlternatives(
            subject, html_message, email_from, recipient_list,)
        email_message.attach_alternative(html_message, "text/html")
        email_message.send()

        admin_message = f"""
            A client sent an inquiry!
            Name : {full_name}
            Email : {email_from}
            Contact : {contact}
            Message : {message}
        """
        inform_admin = EmailMultiAlternatives("CodeHub | Admin", admin_message, email_from, ['garcia.giancarlo714@gmail.com', ])
        inform_admin.send()
        return redirect("/")


# Email Credentials
# email : internationalaluminumfactory@gmail.com
# password :  IAFLiberia!123
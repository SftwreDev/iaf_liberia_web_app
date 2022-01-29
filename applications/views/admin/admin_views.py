from django.shortcuts import render


def admin_page(request):
    template_name = "admin/homepage.html"

    return render(request, template_name)
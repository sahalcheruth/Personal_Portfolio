from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index_view(request):
    return render(request,'port/index.html')

def skill_view(request):
    return render(request,'port/skill.html')

def about_view(request):
    return render(request,'port/about.html')

def resume_view(request):
    return render(request,'port/resume.html')



def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number= request.POST.get('number')
        message = request.POST.get('message')

        # (Optional) Send email or save to database
        subject = f"Contact from {name}"
        full_message = f"From: {name} <{number}> <{email}>\n\n{message}"

        # This assumes email settings are configured
        send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['sahalxcheruth@email.com'])

        success = True

    return render(request, 'port/contact.html', {'success': success})


# def contact_view(request):
#     success = False
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         number= request.POST.get('number')
#         message = request.POST.get('message')

#         # (Optional) Send email or save to database
#         subject = f"Contact from {name}"
#         full_message = f"From: {name} <{number}> <{email}>\n\n{message}"

#         # This assumes email settings are configured
#         send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['sahalxcheruth@gmail.com'])

#         success = True

#     return render(request, 'port/contact.html', {'success': success})

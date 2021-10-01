from django.shortcuts import render
from .models import ContactForm

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def my_resume_view(request):

    
    if request.method == "POST": 
        if "contact" in request.POST: 
            name = request.POST["name"] 
            email = request.POST["email"] 
            subjectt = request.POST["subject"] 
            message = request.POST["message"] 

            form = ContactForm(name=name, email=email, message=message)
            form.save()

            subject = subjectt
            sender = 'Email from ' + name
            body= {
               'name' : 'name: ' + name ,
                'email' : 'email: ' + email ,
                'message' : 'message: ' + message,
            }
            message = '\n'.join(body.values())
            mail_from= settings.EMAIL_HOST_USER
            mail_to= ['faruqabdulsalam@yahoo.com']
            send_mail(
                    subject,
                    message,
                    mail_from,
                    mail_to,
                    fail_silently=False,
                )

    context = {
    }

    return render(request, 'resume.html', context)


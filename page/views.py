from django.shortcuts import render
from .models import ContactForm

# Create your views here.

def my_resume_view(request):

    
    if request.method == "POST": 
        if "contact" in request.POST: 
            name = request.POST["name"] 
            email = request.POST["email"] 
            message = request.POST["message"] 

            form = ContactForm(name=name, email=email, message=message)
            print(form)
            form.save()

    context = {
    }

    return render(request, 'resume.html', context)

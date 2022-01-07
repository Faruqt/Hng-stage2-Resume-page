from django.shortcuts import render

# Create your views here.

def my_resume_view(request):

    context = {
    }

    return render(request, 'resume.html', context)


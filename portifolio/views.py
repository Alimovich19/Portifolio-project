from django.shortcuts import render
from .models import Logo, Skills, Project, Experience, Contact

def home(request):
    logo = Logo.objects.first()
    skills = Skills.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    contacts = Contact.objects.all()
    for skill in skills:
        skill.percentage = int(284 - (skill.percent * 2.84))

    context = {
        'logo': logo,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'contacts': contacts,
    }

    return render(request, 'index.html', context)

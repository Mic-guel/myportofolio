from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Micguel Katili",
        "npm": "2506588065",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS Student at Universitas Indonesia who's still trying to survive. Can't really tell whether I belong here or not, but I'm glad that I can endure this hardship that many people seek"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Micguel Katili",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
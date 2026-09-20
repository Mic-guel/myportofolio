from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Achievement, Project
from main.forms import*


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

def show_achievements(request):
    json_response = get_achievements_json(request)

    achievements = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    achievements = [achievements.object for achievement in achievements]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Micguel Katili",
        "achievement_list": Achievement.objects.all(),
        "title_query": title_query,
    }
    return render(request, "achievement.html", context)

def create_achievement(request):
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new achievement has been successfully added!")
        return redirect("main:show_achievements")

    context = {
        "name": "Micguel Katili",
        "form": form,
    }
    return render(request, "achievements_form.html", context)

def delete_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "Achievement has been successfully deleted")
        return redirect("main:show_achievements")

    return redirect("main:show_achievements")

def get_achievements_json(request):
    title_query = request.GET.get("title", "").strip()
    achievements = Achievement.objects.all()

    if title_query:
        achievements = achievements.filter(title__icontains=title_query)

    achievements_json = serializers.serialize("json", achievements)
    return HttpResponse(achievements_json, content_type="application/json")
    

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Micguel Katili",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new achievement has been successfully added!")
        return redirect("main:show_projects")

    context = {
        "name": "Micguel Katili",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")
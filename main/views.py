import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Achievement, Project
from main.forms import*


def show_main(request):
    last_login = request.COOKIES.get('last_login', "Haven't made a login session/cookie was not found")
    context = {
        "name": "Micguel Katili",
        "npm": "2506588065",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS Student at Universitas Indonesia who's still trying to survive. Can't really tell whether I belong here or not, but I'm glad that I can endure this hardship that many people seek"
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account was made successfully.")
        return redirect("main:login")

    context = {
        "name": "Micguel Katili",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Micguel Katili",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

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
    achievements = [achievement.object for achievement in achievements]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Micguel Katili",
        "achievement_list": achievements,
        "title_query": title_query,
    }
    return render(request, "achievement.html", context)

@login_required
def create_achievement(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required
def delete_achievement(request, achievement_id):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required
def update_project(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied("You don't have the right to change this informations.")

    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:show_main')

    context = {
        'project': project,
    }
    return render(request, 'update_project.html', context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")
import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.views.decorators.http import require_POST

from django.http import JsonResponse

from main.models import Experience, Achievement, Project
from main.forms import*


def show_main(request):
    last_login = request.COOKIES.get('last_login', "Haven't made a login session/cookie was not found")
    is_editor = request.user.groups.filter(name='Editor').exists()

    context = {
        "name": "Micguel Katili",
        "npm": "2506588065",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS Student at Universitas Indonesia who's still trying to survive. Can't really tell whether I belong here or not, but I'm glad that I can endure this hardship that many people seek"
        ),
        "last_login": last_login,
        "is_editor" : is_editor,
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
    is_editor = request.user.groups.filter(name='Editor').exists()

    context = {
        "name": "Micguel Katili",
        "experience_list": Experience.objects.all(),
        "is_editor" : is_editor,
    }
    return render(request, "experience.html", context)

def show_achievements(request):
    is_editor = request.user.groups.filter(name='Editor').exists()

    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Micguel Katili",
        "title_query": title_query,
        "is_editor" : is_editor,
        "form" : AchievementForm(),
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
    achievements = Achievement.objects.prefetch_related('starred_by').all()

    if title_query:
        achievements = achievement.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for achievement in achievements:
        starred_users = achievement.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(achievement.id),
            "fields": {
                "title": achievement.title,
                "description": achievement.description,
                "month_year": achievement.month_year,
                "achievement_image_url": achievement.achievement_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    return JsonResponse(data, safe=False)
    

def show_projects(request):
    is_editor = request.user.groups.filter(name='Editor').exists()

    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Micguel Katili",
        "title_query": title_query,
        "is_editor" : is_editor,
        "form" : ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required
def create_project(request):
    is_editor = request.user.groups.filter(name='Editor').exists()
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
        "is_editor" : is_editor,
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
def edit_project(request, project_id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied("You don't have the right to change this informations.")

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:show_projects')

    context = {
        'project': project,
        'form' : form,
        'name' : "Micguel Katili",
        "is_editor" : is_editor,
        
    }
    return render(request, 'edit_project.html', context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_achievement_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = AchievementForm(request.POST)
    if form.is_valid():
        achievement = form.save()
        return JsonResponse(
            {"message": "Achievement successfully added.", "pk": str(achievement.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
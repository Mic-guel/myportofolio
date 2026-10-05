from django.urls import path

from main.views import*

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),

    path("achievement/add/", create_achievement, name="create_achievement"),
    path("achievement/", show_achievements, name="show_achievements"),
    path("api/achievements/", get_achievements_json, name="get_achievements_json"),
    path("achievements/<uuid:achievement_id>/delete/",delete_achievement, name="delete_achievement"),
    path("achievements/add-ajax/", create_achievement_ajax, name="create_achievement_ajax"),

    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("projects/edit/<uuid:project_id>/", edit_project, name="edit_project"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
]
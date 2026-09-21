from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import*

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Project's Name",
            "description": "Project's Description",
            "project_url": "Supporting Project's URL",
            "project_image_url": "Project Picture's URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe the project.",
                    "rows": 3,
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/",
                }
            ),
        }

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = [
            "title",
            "description",
            "achievement_image_url",
        ]

        labels = {
            "title": "Achievement's Name",
            "description": "Achievement's Description",
            "achievement_image_url": "Achievement Picture's URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe the Achievement.",
                    "rows": 3,
                }
            ),
            "achievement_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/",
                }
            ),
        }
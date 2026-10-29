from django import forms

from .models import Project, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["project", "title", "description", "status", "due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name","description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
from django import forms
from todolist.models import TaskItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = ['title', 'description']
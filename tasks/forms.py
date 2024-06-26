from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['documentId', 'nombres', 'apellidos', 'empresa', 'date_ini', 'date_end', 'important']

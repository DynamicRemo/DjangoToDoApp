from django import forms
from.models import apptodo

class AddTodoForm(forms.ModelForm):
    class Meta:
        model = apptodo
        fields = ["title", "done"]
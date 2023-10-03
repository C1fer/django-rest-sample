from django import forms

class AddProjectForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    technology = forms.CharField(max_length=20)

from django import forms
from .models import Articles

class produitform(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ['id','prix_total']

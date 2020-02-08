from django import forms
from .models import Course
from pyuploadcare.dj.forms import ImageField, FileWidget

class CourseForm(forms.ModelForm):
    image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
    class Meta:
        model=Course
        fields=('title', 'desc', 'number_of_hours', 'instructor', 'image', 'cost')
        
        
class CourseSearchForm(forms.Form):
    search_terms = forms.CharField(required=False)
    min_cost = forms.FloatField(required=False, min_value=0)
    max_cost = forms
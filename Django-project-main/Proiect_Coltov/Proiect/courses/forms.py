from django import forms
from .models import Course, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'materials']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Course title'}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'rows': 4, 'placeholder': 'Course description'}),
            'price': forms.NumberInput(attrs={'class': 'input-field', 'step': 0.01, 'placeholder': 'Price'}),
            'materials': forms.ClearableFileInput(attrs={'class': 'input-file'}),
        }
    
    def clean_materials(self):
        file = self.cleaned_data.get('materials')

        if not file:
            raise forms.ValidationError("You must upload a file.")

        return file


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
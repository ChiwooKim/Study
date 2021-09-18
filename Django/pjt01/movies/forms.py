from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title',
            }
        )
    )

    overview = forms.CharField(
        label = 'Overview',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the overview',
            }
        )
    )
    
    poster_path = forms.CharField(
        label = 'Poster path',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the poster path',
            }
        )
    )


    class Meta:
        model = Movie
        fields = '__all__'
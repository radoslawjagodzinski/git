from django import forms
from testowa.models import Movie, Genre

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ("created_on",)
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ("created_on",)
    def clean_name(self):
        name = self.cleaned_date["name"]
        if "curse" in name.lower():
            raise forms.ValidationError("You can not use forbidden words")
        return name
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
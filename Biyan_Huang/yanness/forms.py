from django import forms
from .models import Movie
from .models import Review
from django.contrib.auth.forms import UserCreationForm


class comicForm(forms.Form):
    id = forms.IntegerField(min_value=0, max_value=1000, label="Enter a Random ID")


class dogForm(forms.Form):
    breed = forms.CharField(max_length=30, label="Enter Breed")
    subreed = forms.CharField(max_length=30, label="Enter Subreed")


class qrForm(forms.Form):
    height = forms.IntegerField(min_value=0, max_value=300, label="Enter Height")
    width = forms.IntegerField(min_value=0, max_value=300, label="Enter Width")
    info = forms.CharField(max_length=100, label="Enter Your Message")


class movieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ['posted_by', 'last_updated', 'created_by']
    # name = forms.CharField(max_length=120, label="Movie Name", required=False)
    # description = forms.CharField(max_length=100000, label="Movie Description", required=False)
    # year = forms.IntegerField(min_value=1900, label="Released Year", required=False)
    # rating = forms.FloatField(min_value=0, max_value=10, label="Movie Rating", required=False)


class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
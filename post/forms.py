from django import forms
from .models import Post, Semester
import datetime


def current_year():
    return datetime.date.today().year


def year_choices():
    return [(r, r) for r in range(current_year()-10, current_year()+1)]


class PostForm(forms.ModelForm):
    semester = forms.ModelChoiceField(
        queryset=Semester.objects.all(), to_field_name='semester')
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    email = forms.EmailField(disabled=True)
    duration = forms.IntegerField(help_text="months")
    year = forms.TypedChoiceField(
        coerce=int, choices=year_choices, initial=current_year)

    class Meta:
        model = Post

        fields = ['title', 'email',
                  'company', 'role', 'industry',
                  'duration',
                  'semester', 'year', 'salary',
                  'review', 'rating']

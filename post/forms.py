from django import forms
from .models import Post, Semester


class PostForm(forms.ModelForm):
    semester = forms.ModelChoiceField(queryset=Semester.objects.all())
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    email = forms.EmailField(disabled=True)
    duration = forms.IntegerField(help_text="months")

    class Meta:
        model = Post

        fields = ['title', 'email',
                  'company', 'role', 'industry',
                  'duration',
                  'semester', 'year', 'salary',
                  'industry', 'review', 'rating']

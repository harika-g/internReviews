import django_filters
from .models import Post, Semester
from django import forms


class PostFilter(django_filters.FilterSet):
    # salary = django_filters.NumberFilter()
    # salary__gt = django_filters.NumberFilter(
    #     field_name='salary', lookup_expr='gt')
    # salary__lt = django_filters.NumberFilter(
    #     field_name='salary', lookup_expr='lt')

    title__name = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains')
    role__name = django_filters.CharFilter(
        field_name='role', lookup_expr='icontains')
    industry__name = django_filters.CharFilter(
        field_name='industry', lookup_expr='icontains')
    company_names = Post.objects.values_list('company', flat=True).distinct()
    company_choices = [(choice, choice) for choice in company_names]
    company__name = django_filters.ChoiceFilter(
        field_name='company', choices=company_choices, label="Company", empty_label="All companies",
        widget=forms.Select(attrs={'class': 'form-control'}),)

    rating__filter = django_filters.MultipleChoiceFilter(field_name='rating',
                                                         choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), label='Rating', widget=forms.CheckboxSelectMultiple)

    semester__name = django_filters.ModelChoiceFilter(field_name='semester',
                                                      queryset=Semester.objects.all(), empty_label="All Semesters",
                                                      label="Semester",
                                                      widget=forms.Select(attrs={'class': 'form-control'}),)

    class Meta:
        model = Post
        fields = [
            # 'company', 'role', 'industry',
            # 'salary',
        ]

from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(label='Natrícula:', max_length=10, widget=forms.TextInput({'class': 'form-control'}))

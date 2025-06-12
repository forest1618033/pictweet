from .models import Tweet
from django import forms

class TweetForm(forms.ModelForm):
    class Meta:
      model = Tweet
      fields = ['image', 'text']
      widgets = {
         #'name': forms.TextInput(attrs={'placeholder': 'Nickname'}),
         'text': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 10}),
      }
      labels = {
         #'name':'Nickname',
         'text': 'テキスト',
      }

class SearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '投稿を検索する',
            'class': 'search-input'
        })
    )
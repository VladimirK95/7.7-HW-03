from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=10)
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'title',
            'text',
        ]


    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if text == title:
            raise ValidationError(
                "Текст не должен быть идентичным названию."
            )

        return cleaned_data

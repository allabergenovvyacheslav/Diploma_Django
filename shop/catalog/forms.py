from django import forms
from .models import *


# Простая форма не связанная с моделями (Форма обратной связи с клиентом)
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Ваш Email")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")


# Создание формы для отзывов
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'comment']  # Поля для заполнения
        widgets = {'comment': forms.Textarea(attrs={'rows': 4})} # «rows» (количество строк) 4

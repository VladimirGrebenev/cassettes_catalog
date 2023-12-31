from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms

from .models import CollectorFeedback

User = get_user_model()


#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    username = forms.CharField(label='search',
                        widget=forms.TextInput(attrs={'placeholder': _('Username')}))
    email = forms.CharField(label='search',
                               widget=forms.TextInput(attrs={'placeholder': _('Email')}))
    password1 = forms.CharField(label='search',
                               widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))
    password2 = forms.CharField(label='search',
                                 widget=forms.PasswordInput(attrs={'placeholder': _('Password repeat')}))

    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-cust modal__input'


class ProfileForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'born_date', 'country', 'image', 'language', 'website', 'bio', 'premium')
        labels = {
            'bio': 'О себе',
        }
        help_texts = {
            'born_date': 'Формат записи (2023-12-31)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({'class': 'input-cust input-cust_fz14'})
        self.fields['language'].widget.attrs.update({'class': 'input-cust input-cust_fz14'})


class CollectorFeedbackForm(forms.ModelForm):
    rating_score = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={
            'class': 'input-cust',
            'placeholder': _('Rate collector'),
        }),
        label=_('Rating score')
    )
    feedback = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'textarea-cust',
                'placeholder': _('Leave feedback'),
                'rows': '2',
            }
        ),
        label=_('Feedback')
    )

    class Meta:
        model = CollectorFeedback
        fields = ('user', 'collector', 'rating_score', 'feedback') #'user', 'collector',



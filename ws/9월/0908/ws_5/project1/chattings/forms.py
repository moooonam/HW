from django import forms
from .models import Chat


class ChattingForm(forms.ModelForm):
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placehoder':'Nickname',
                'maxlength':10,
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Chat!',
                'rows':5,
                'cols':50,

            }
        )
    )
    class Meta:
        model = Chat #어떤 모델을 기반으로 할지
        fields = '__all__'
  
from django.contrib.auth.forms import (
    AuthenticationForm
)
from django import forms
from .models import introducer



class IntroducerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.label = ""  #labelを無くすため　もっと他にいい方法があるのかも　
    class Meta:   
        model = introducer
        fields = '__all__'

IntroducerFormSet = forms.modelformset_factory(
    introducer, form=IntroducerForm, extra=10
)

class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        word_list = ['メールアドレス', 'パスワード']
        i = 0   #インスタンスとして利用しないのでselfをつけていないが文法的に問題があるのか、ないのか？
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.label = word_list[i]
            i += 1

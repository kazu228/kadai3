from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
)
from django import forms
from .models import introducer
from django.contrib.auth import get_user_model

User = get_user_model()


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

class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = (User.USERNAME_FIELD,)  # ユーザー名として扱っているフィールドだけ、作成時に入力する

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
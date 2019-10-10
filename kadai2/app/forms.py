from django.contrib.auth.forms import (
    AuthenticationForm
)
from django import forms
from .models import introducer

# class IntroducerForm(forms.Form):
    
#     department = forms.CharField(label="department", required=False)
#     division = forms.CharField(label="division" , required=False)
#     name = forms.CharField(label='name' , required=False)
#     mail = forms.EmailField(label='mail' , required=False)

#     class Meta:
#         model = introducer
#         fields = '__all__'
        
class IntroducerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

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
        i = 0
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.label = word_list[i]
            i += 1
            # field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
            
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import IntroducerForm
from django.contrib.auth.decorators import login_required
from .models import introducer
from django.shortcuts import redirect
from django.core.mail import send_mail
from email.mime.text import MIMEText
import smtplib
from random import choice
from string import ascii_letters, digits, punctuation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponse
from .forms import IntroducerFormSet
import re

def gen_passwd(length=8, chars=ascii_letters+digits+punctuation):
    # passwordを生成する関数、8文字のランダムな英数字を返す
    return ''.join([choice(chars) for i in range(length)])
 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
    else:

        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def confirm(request):
    # メール本文を確認するページ表示の関数
    return render(request, 'app/confirm.html')


@login_required
def form(request):
    formset = IntroducerFormSet(request.POST or None ,queryset=introducer.objects.none())
    
    if request.method == 'POST' and formset.is_valid(): #request.method != 'POST' or not formset.is_valid():
        mail_list = []                                  #の短いコードの方で条件分岐した方が読みやすい
    
        for k in request.POST:
            if  re.search('form-\d-mail', k) and request.POST[k] != '':
                mail_list.append(request.POST[k])  

        formset.save()

        from_email="kskkm0228@gmail.com"
        from_password="KY02282621"

        # to_email= mail

    #メールの内容
        subject="Test"
        url = "127.0.0.1:8000/app/"
        
        for i in range(len(mail_list)):
            password = gen_passwd(8, ascii_letters+digits)
            message="いつも優秀な人材を紹介してくれてありがとうございます。\
                これからも、我が社に入ってく れそうな人材をぜひともご紹介ください。\
                List of Excellent Young-manは、みなさんから人事部に 紹介してもいい\
                と思った人たちを登録いただくシステムです。もし人事部から連絡してもよい優秀な方\
                がいらっしゃいましたら、ぜひご登録をお願いします <br> URL:" + url + "<br> \
                パスワード：" + password
            msg=MIMEText(message, "html")
            msg["Subject"]=subject
            msg["To"]=mail_list[i]
            msg["From"]=from_email
            gmail=smtplib.SMTP("smtp.gmail.com", 587)
            gmail.starttls()
            gmail.login(from_email, from_password)
            gmail.send_message(msg)

        
        return redirect(to='/app')

    params = {
            'title': '紹介者情報を登録',
            'message': '情報の登録とメールも送信します。',
            'formset': formset
        }

    return render(request, 'app/form.html', params)


@login_required
def top(request):
    data = introducer.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'app/top.html', params)

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'app/login.html'
    def post(self, request, *args, **kwargs):
        params = {
            'message': "",
            'form': LoginForm,
            'item': [
                'メールアドレス', 'パスワード'
            ]
        }
        password = request.POST["password"]
        if re.search('[A-Z]+', password):
            params['message'] = "Caps Lockキーがオンになっていませんか？"
            return render(request, 'app/login.html', params)
        form_class = LoginForm
        template_name = 'app/login.html'
        return super().post(self, request, *args, **kwargs)
    

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'app/top.html'
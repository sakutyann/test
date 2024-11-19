from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

from django.views import View
from django.contrib.auth import login, logout
from django.contrib import messages
import logging
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin


logger = logging.getLogger(__name__)



# サインアップ
class SignUpView(CreateView):
    """サインアップページのビュー"""
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    
    # サインアップ完了後のリダイレクト先
    success_url = reverse_lazy('team:main')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        
        # 新規ユーザーをログインさせる
        login(self.request, user)
        
        # セッションが正しく維持されるように保存
        # self.request.session.modified = True
        # self.request.session.save()
        
        logger.info(f"User {user.username} logged in successfully after signup.")
        
        # return redirect(self.success_url)
    
        # ログイン成功をURLパラメータとして渡す
        return redirect(f'{self.success_url}?loginStatus=success&username={user.username}')






# ログイン
class SignInView(TemplateView):
    """ログインページのビュー"""
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        logger.info("SignInView post method has been called.")
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            logger.info("User authenticated successfully.")
            login(request, form.get_user())
            logger.info("Session user: %s", request.user.username)
            
            
            # return redirect('team:main')  # ログイン後の画面
        
            # ログイン成功をURLパラメータとして渡す
            return redirect(f'/main?loginStatus=success&username={form.get_user().username}')
        
        else:
            messages.error(request, "ユーザーネームまたは、パスワードが間違っています。")
            logger.warning("Authentication failed with errors: %s", form.errors)
            return render(request, self.template_name, {'login_form': form})






# アカウント情報閲覧
@method_decorator(login_required, name='dispatch')
class AccountInfoView(View):
    """ユーザーのアカウント情報を表示するビュー"""

    def get(self, request):
        """GETリクエストでユーザー名とメールアドレスを表示"""
        return render(request, 'account_info.html', {
            'username': request.user.username,
            'email': request.user.email
        })






# # メインページのビュー
# def main_view(request):
#     return render(request, 'main.html')



# ログアウト
@login_required
def logout_view(request):
    user_info = f"ログイン中: {request.user.username}" if request.user.is_authenticated else "ログインしていません"
    return render(request, 'logout_check.html', {'user_info': user_info})

def logoutok_view(request):
    logout(request)
    user_info = "正常にログアウトされました"
    return render(request, 'logout_ok.html', {'user_info': user_info})


  
        
# test
def test(request):
    if request.user.is_authenticated:
        user_info = f"Logged in as {request.user.username}"
    else:
        user_info = "Not logged in"
    
    return render(request, 'test.html', {'user_info': user_info})


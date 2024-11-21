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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import json
import logging
from django.contrib.auth import update_session_auth_hash

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

@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # JSONデータを取得
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            user = CustomUser.objects.get(id=request.user.id)

            # 変更された場合のみ更新
            if username and username != user.username:
                user.username = username
            
            if email and email != user.email:
                user.email = email
            
            if password:  # パスワードが新しい場合のみ
                user.set_password(password)

            # 常に保存を実行（フィールドが更新された場合、Djangoは最適化して必要な部分だけを更新します）
            user.save()

            # パスワードが変更された場合はセッションを更新
            if password:
                update_session_auth_hash(request, user)

            return JsonResponse({'success': True, 'message': '更新が完了しました'})

        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'ユーザーが見つかりません'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': '無効なリクエストです'})
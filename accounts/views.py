
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

import logging
logger = logging.getLogger(__name__)

class SignUpView(CreateView):
    """サインアップページのビュー
    """

# forms.pyで定義したフォームのクラス
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = "signup.html"
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        
        """「CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録を行う
        
        paramenters:
            form(django.forms.Form):
            form classに格納されているCustomUserCreationFormオブジェクト
        Return:
          HttpResponseRedirect オブジェクト:
          スーパークラスのform_valid()の戻り値を返すことで、
          success _urlで設定されているURLにリダイレクトさせる
        """
        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save ()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    """サインアップ完了ページのビュー
    """
    # レンダリングするテンプレート
    template_name = "signup_success.html"




# irann
    
class SignInView(TemplateView):
    """ログインページのビュー"""
    template_name = "signup.html"
    
    def post(self, request, *args, **kwargs):
        
        logger.info("SignInView post method has been called.")
        # POSTデータの確認
        logger.info("POST data: %s", request.POST)
        print("SignInView post method has been called.")
        # ログイン処理を行う
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            # ユーザー認証成功確認
            logger.info("User authenticated successfully.")
            # ログインさせる
            login(request, form.get_user())
            # セッションが更新されたか確認するためのログ出力
            logger.info("Session user: %s", request.user.username)                        
            # ログイン後のリダイレクトを設定
            return redirect('team:main') #ログイン後の画面
        
        else:
            # エラーメッセージ
            logger.warning("Authentication failed with errors: %s", form.errors)
            return render(request, self.template_name, {'login_form': form})



# test
def test(request):
    if request.user.is_authenticated:
        user_info = f"Logged in as {request.user.username}"
    else:
        user_info = "Not logged in"
    
    return render(request, 'test.html', {'user_info': user_info})

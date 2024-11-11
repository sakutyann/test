from django.urls import path
# viewsモジュールをインポート
# from django.contrib.auth.views import LoginView
# from django.contrib.auth. import views as auth_views
from . import views


# from django.contrib.auth import views as auth_views

app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # viewsモジュールのSignupViewsをインスタンス化する
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    # サインアップ完了ページのビューの呼び出し
    # http(s)://＜ホスト名＞/signup_succes｝へのアクセスに対して、
    # viewsモジュールのSignupViewsをインスタンス化する
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    
    
    # ログインのURL設定
    path('signin/', views.SignInView.as_view(), name='signin'),
    
    # test
    path('test/', views.test, name="test"),
    

]

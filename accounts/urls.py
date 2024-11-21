from django.urls import path
# viewsモジュールをインポート
from django.contrib.auth import views as auth_views
# from django.contrib.auth. import views as auth_views
from . import views
# from team.views import MainView


# from django.contrib.auth import views as auth_views

app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # ログインのURL設定
    path('signin/', views.SignInView.as_view(), name='signin'),
    # アカウント情報閲覧
    path('account_info/', views.AccountInfoView.as_view(), name='account_info'),
    # ログアウト確認
    path('logout_check/', views.logout_view, name='logout_check'),
    # ログアウト完了
    path('logout_ok/', views.logoutok_view, name='logout_ok'),
    
    # test
    path('test/', views.test, name="test"),

]

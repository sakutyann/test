# formapp/urls.py
from django.urls import path
from . import views

app_name = 'formapp' 

urlpatterns = [
    path('quest_form/', views.quest_form_view, name='quest_form'), #クエスト登録画面
    path('quest_register/<int:quest_id>/', views.quest_register_view, name='quest_register'), #お題登録画面
    path('success/', views.quest_success_view, name='quest_success'),  # 登録成功画面
]




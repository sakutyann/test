from django.urls import path
from . import views
from .views import MainView
from team.views import QuestDetailView


app_name = 'team'


urlpatterns = [path('', views.title_view, name='title'),#タイトル画面                
               path('main/', MainView.as_view(), name="main"),#main画面(クエスト一覧)
               path('quest/<int:pk>/', views.QuestDetailView.as_view(), name='quest_detail'),#クエスト詳細画面
               path('questdo/', views.QuestDetailView.as_view(), name='quest_detail'),#クエスト詳細画面
               path('quest_challenge/<int:pk>/', views.QuestChallengeView.as_view(), name='quest_challenge'),# クエスト挑戦画面
               path('quest_challenge/', views.QuestChallengeView.as_view(), name='quest_challenge'),#クエスト挑戦画面
               

               path('coupon/', views.couponformworldfunction, name='coupon'),
              #  path('couponuse/', views.couponuseformworldfunction),
              #  path('couponend/', views.couponendformworldfunction),
              #  path('couponpast/', views.couponpastformworldfunction),
           
              #  path('questlook/', views.questlookformworldfunction),
              #  path('couponnot/', views.couponnotformworldfunction),
              #  path('questok/', views.questokformworldfunction),
              #  path('quester/', views.questerformworldfunction),
              #  path('newaccount/', views.newaccountformworldfunction),
             ]

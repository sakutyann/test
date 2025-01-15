
from django.urls import path
from . import views

app_name = 'userquest'

urlpatterns = [path('questnow/', views.questnowformworldfunction, name='questnow'),
               path('questnot/', views.questnotformworldfunction, name='questnot'),
            #    path('questdo/', views.questdoformworldfunction, name='questdo'),
               path('quest_challenge/', views.quest_challenge_view, name='quest_challenge'),
               path('questgo/<int:pk>/', views.QuestGoView.as_view(), name='questgo'),               
               path('questgo/', views.QuestGoView.as_view(), name='questgo'),
               path('questyes/<int:pk>/', views.QuestYesView.as_view(), name='questyes'),# クエスト挑戦画面
               path('questyes/', views.QuestYesView.as_view(), name='questyes'),#クエスト挑戦画面
               path('questout/<int:pk>/', views.QuestOutView.as_view(), name='questout'),
               path('questout/', views.QuestOutView.as_view(), name='questout'),
               path('questfin/', views.QuestFinView.as_view(), name='questfin'),
               path('coupons/<int:coupon_id>/detail', views.coupon_detail, name='coupon_detail'),  # クーポン詳細
               path('coupons/used/', views.used_coupons, name='used_coupons'),  # 使用済みクーポン
               path('coupons/complete/', views.coupon_complete, name='coupon_complete'),  # クーポン使用完了
               ]
# Create your tests here.

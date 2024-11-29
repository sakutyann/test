
from django.urls import path
from . import views

app_name = 'userquest'

urlpatterns = [path('questnow/', views.questnowformworldfunction, name='questnow'),
               path('questnot/', views.questnotformworldfunction, name='questnot'),
            #    path('questdo/', views.questdoformworldfunction, name='questdo'),
               path('questgo/', views.questgoformworldfunction, name='questgo'),
               path('questyes/', views.questyesformworldfunction, name='questyes'),
               path('questout/', views.questoutformworldfunction, name='questout'),
               path('questfin/', views.questfinformworldfunction, name='questfin'),
               path('coupon/', views.coupon_list, name='coupon'),  # クーポン一覧
               path('coupons/<int:coupon_id>/detail', views.coupon_detail, name='coupon_detail'),  # クーポン詳細
               path('coupons/used/', views.used_coupons, name='used_coupons'),  # 使用済みクーポン
               path('coupons/complete/', views.coupon_complete, name='coupon_complete'),  # クーポン使用完了
               ]
# Create your tests here.

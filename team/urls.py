from django.urls import path
from . import views
from .views import MainView



app_name = 'team'


urlpatterns = [path('', views.title_view, name='title'),#タイトル画面                
               path('main/', MainView.as_view(), name="main"),#main画面(クエスト一覧)
               path('form/', views.formworldfunction,name='form'),#クエスト依頼フォーム
               path('questform/', views.questformworldfunction,name='questform'),#お題登録フォーム

               path('coupon/', views.couponformworldfunction, name='coupon'),
               path('couponuse/', views.couponuseformworldfunction),
               path('couponend/', views.couponendformworldfunction),
               path('couponpast/', views.couponpastformworldfunction),
           
               path('questlook/', views.questlookformworldfunction),
               path('couponnot/', views.couponnotformworldfunction),
               path('questok/', views.questokformworldfunction),
               path('quester/', views.questerformworldfunction),
               path('newaccount/', views.newaccountformworldfunction),
              #  進行中クエスト
               path('questnow/', views.questnowformworldfunction, name='questnow'),
               path('questnot/', views.questnotformworldfunction),
               path('questdo/', views.questdoformworldfunction),
               path('questgo/', views.questgoformworldfunction),
               path('questyes/', views.questyesformworldfunction),
               path('questout/', views.questoutformworldfunction),
               path('questfin/', views.questfinformworldfunction),
               ]

from django.urls import path
from . import views
from .views import MainView



app_name = 'team'


urlpatterns = [path('login/', views.loginworldfunction),
              #  main
               path('main/', MainView.as_view(), name="main"),
               path('account/', views.accountworldfunction),
               path('logout/', views.logoutworldfunction),
               path('logoutok/', views.logoutokworldfunction),
               #クエスト依頼フォーム
               path('form/', views.formworldfunction,name='form'),
               #お題登録フォーム
               path('questform/', views.questformworldfunction,name='questform'),
               
               path('coupon/', views.couponformworldfunction, name='coupon'),
               path('couponuse/', views.couponuseformworldfunction),
               path('couponend/', views.couponendformworldfunction),
               path('couponpast/', views.couponpastformworldfunction),
               path('tittle/', views.tittleformworldfunction),
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

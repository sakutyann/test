from django.urls import path
from . import views

<<<<<<< HEAD
=======
app_name = 'team'
>>>>>>> bad7c866ff6de21db0e99333e94c10d3967ae660

urlpatterns = [path('login/', views.loginworldfunction),
               path('main/', views.mainworldfunction, name="main"),
               path('account/', views.accountworldfunction),
               path('logout/', views.logoutworldfunction),
               path('logoutok/', views.logoutokworldfunction),
               path('form/', views.formworldfunction),
               path('quest/', views.questformworldfunction),
               path('coupon/', views.couponformworldfunction),
               path('couponuse/', views.couponuseformworldfunction),
               path('couponend/', views.couponendformworldfunction),
               path('couponpast/', views.couponpastformworldfunction),
               path('tittle/', views.tittleformworldfunction),
               path('questlook/', views.questlookformworldfunction),
               path('couponnot/', views.couponnotformworldfunction),
               path('questok/', views.questokformworldfunction),
               path('quester/', views.questerformworldfunction),
               path('newaccount/', views.newaccountformworldfunction),
               path('questnow/', views.questnowformworldfunction),
               path('questnot/', views.questnotformworldfunction),
               path('questdo/', views.questdoformworldfunction),
               path('questgo/', views.questgoformworldfunction),
               path('questyes/', views.questyesformworldfunction),
               path('questout/', views.questoutformworldfunction),
               path('questfin/', views.questfinformworldfunction),
               ]

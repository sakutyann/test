
from django.urls import path
from . import views

app_name = 'userquest'

urlpatterns = [path('questnow/', views.questnowformworldfunction, name='questnow'),
               path('questnot/', views.questnotformworldfunction, name='questnot'),
               path('questdo/', views.questdoformworldfunction, name='questdo'),
               path('questgo/', views.questgoformworldfunction, name='questgo'),
               path('questyes/', views.questyesformworldfunction, name='questyes'),
               path('questout/', views.questoutformworldfunction, name='questout'),
               path('questfin/', views.questfinformworldfunction, name='questfin'),
               ]
# Create your tests here.

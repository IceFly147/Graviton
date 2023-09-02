from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about, name='about'),
    path('generate/',views.generate,name="generate"),
    path('roadmap/',views.result,name="check"),
    #Made by IceFly147
    path('dev/',views.stuff),
    path('cookie/', views.setCookie, name="cookie")
 
]
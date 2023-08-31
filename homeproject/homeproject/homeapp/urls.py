from . import views
from django.urls import path

urlpatterns = [

    path('',views.home1,name='home'),
    # path('cal/',views.calculate,name='calculate'),
    # path('result/',views.result,name='result'),
    # path('add/',views.addition,name='addition'),
    # path('sub/',views.subtraction,name='subtraction'),
    # path('mul/',views.multiplication,name='multiplication'),
    # path('div/',views.division,name='division'),
    # path('about/',views.about,name='about'),

]
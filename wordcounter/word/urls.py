from django.urls import path

from .views import *
from . import views
urlpatterns=[
    path('', MainpageView.as_view(), name='mainpage'),
    path('word/home/',views.home, name='home'), #name은 url의 이름을 설정한다.
    path('word/about/',views.about, name='about'),
    path('word/result/',views.result, name='result'),

]
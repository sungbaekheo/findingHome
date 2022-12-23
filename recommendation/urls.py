from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('main/',views.main_page, name='main_page'),
    path('rec/',views.recommender, name='recommender'),
]
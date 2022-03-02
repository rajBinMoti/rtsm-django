from django.urls import include, re_path
from website import views

urlpatterns = [
    re_path('', views.HomePageView.as_view(), name='home'),
    re_path('about/', views.AboutPageView.as_view(), name='about'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_home_view),
    path('<slug:articlename>/', views.dynamic_article),
]
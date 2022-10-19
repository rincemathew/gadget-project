from django.urls import path, re_path

from . import views

urlpatterns = [
    path('api/release/', views.ReleaseResultsView.as_view()),   #rest api
  
]
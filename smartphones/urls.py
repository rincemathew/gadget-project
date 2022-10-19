from django.urls import path

from . import views, apiview

urlpatterns = [
    path('', views.home_view),
    path('<slug:brand_url>/<slug:mobile_url>/', views.mobiles_details),
    path('<slug:listmobile>/', views.mobiles_list),
    path('api/mobilelist', apiview.MobileListView.as_view()),
]
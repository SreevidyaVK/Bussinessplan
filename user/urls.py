from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('purpose/', views.purpose, name="purpose"),
    path('activity', views.activity, name="activity")
]
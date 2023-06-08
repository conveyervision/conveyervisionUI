from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('config/', views.config, name='config'),
# API URLs
    path('api/cvspots/', views.CvSpotsList.as_view()),
    path('api/cvspots/<int:pk>/', views.CvSpotsDetail, name='CvSpotsDetail'),
]


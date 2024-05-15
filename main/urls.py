from django.contrib import admin
from django.urls import path, include

from movies_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact/', views.contact),
    path('about/', views.about),
    path('joinus/', views.joinus),
    path('review/', views.review),
    path('single/<int:id>', views.single),
    path('single/new_review', views.submit_review),
    path('accounts/', include("django.contrib.auth.urls")),
    path("profile", views.profile_views, name='profile')
]

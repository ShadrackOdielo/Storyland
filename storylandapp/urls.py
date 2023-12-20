# storylandapp/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import book_detail, user_profile, bookshelf, home_view, register_view, user_dashboard

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('user/<str:username>/', user_profile, name='user_profile'),
    path('user/<str:username>/shelf/<str:shelf_name>/', bookshelf, name='bookshelf'),
]

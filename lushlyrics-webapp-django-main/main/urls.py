from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),

    # authentication urls
    path("signup", views.singup, name='signup'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("reset_password", views.password_reset, name='reset_password'),
    path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", views.password_reset_confirm, name='password_reset_confirm'),
    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]
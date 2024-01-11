from django.contrib.auth import views as auth_views
from django.urls import path

from account import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    # login logout
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path("logout-then-login/", views.logout_then_login,
         name="logout_then_login"),
    # change password
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # reset password
    # # restore password urls
    # path(
    #     "password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    # ),
    # path(
    #     "password-reset/done/",
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "password-reset/confirm/<uidb64>/<token>/",
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password-reset/complete/",
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]

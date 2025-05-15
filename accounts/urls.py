from django.urls import path
from accounts import views

app_name='accounts'

urlpatterns = [
    path('login/',views.CustomLoginView.as_view() ,name='login'),
    path('logout/',views.CustomLogoutView.as_view(),name='logout'),
    path('signup/',views.CustomSignupView.as_view(),name='signup'),
    path("password/reset/", views.CustomPasswordRest.as_view(), name="reset_password"),
    path("password/reset/done/", views.CustomPasswordDone.as_view(), name="reset_password_done"),
    path("password/rest/confirm/<uidb64>/<token>", views.CustomPasswordConfirm.as_view(), name="reset_password_confirm"),
    path("password/reset/complate/", views.CustomPasswordComplete.as_view(), name="reset_password_complete"),
]

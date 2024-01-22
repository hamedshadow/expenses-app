from .views import RegisterationView,UsernameValidationView,EmailValidationView,VerificationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect


urlpatterns = [
    path('register', RegisterationView.as_view(),name="register"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),name="validate_email"),
    path('activate/<uidb64>/<token>', (VerificationView.as_view()),name="activate"),
]

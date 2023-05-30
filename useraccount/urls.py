from django.urls import path
from useraccount.views import UserRegistration,UserLogin,UserProfile,UserChangePassword,SendPasswordResetEmail,UserPasswordReset
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('changepassword/', UserChangePassword.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmail.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordReset.as_view(), name='reset-password'),

]
from django.urls import path
from .views import index, other_page, BBLoginView, \
    profile, BBLogoutView, BBPasswordChangeView


app_name = 'main'
urlpatterns = [
    path('account/password/change', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]

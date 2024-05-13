from django.urls import path

from account.views import AccountUpdateView, my_logout

app_name = 'account'

urlpatterns = [
    path('', AccountUpdateView.as_view(), name='update'),
    path('logout/', my_logout, name='logout'),
]
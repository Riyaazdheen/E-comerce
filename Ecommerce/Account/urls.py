from django.urls import path
from .views import signin, signup, signout

app_name = 'account'

urlpatterns = [
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('signout', signout, name='signout')
]

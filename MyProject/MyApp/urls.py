from django.conf.urls import url
from . import views

#Template Tagging
app_name = 'MyApp'

urlpatterns = [
    url(r'^users/$',views.users,name='users'),
    url(r'^list/$',views.list,name='list'),
    url(r'^thankyou/$',views.thankyou,name='thankyou')
]

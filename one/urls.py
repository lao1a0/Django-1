from django.conf.urls import url
from one import views
from one.views import CreateStudent

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^print/',views.PrintTable,name='print'),
    url(r'^studentname/(\d+)/',views.stuname,name='studentname'),
    url(r'^detail/',views.detail,name='detail'),
    url(r'^CreateStudent/', views.CreateStudent,name='CreateStudent'),
]





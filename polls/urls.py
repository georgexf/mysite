from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('school/', views.index, name='index1'),
    url('school/<int:school_id>/',views.school_detail, name='school_detail'),
]
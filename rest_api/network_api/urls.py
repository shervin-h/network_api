from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('networks', views.get_networks_info, name='networks')

]


from django.urls import path

from apps.views import index_view, get_param_view, myme_view, calculator_view, users_list_view

urlpatterns = [
    path('index' , index_view),
    path('get_param' , get_param_view),
    path('myme' , myme_view),
    path('cal' , calculator_view),
    path('users' , users_list_view)
]

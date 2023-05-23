
from django.urls import path
from support.api.views import *
urlpatterns = [
    path('create/',SupportCreateAPI.as_view(),name='support-create')
]

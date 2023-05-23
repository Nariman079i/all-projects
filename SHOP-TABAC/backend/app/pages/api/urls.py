from django.urls import path
from pages.api.views import *

urlpatterns = [
    path('main/',PageViewAPI.as_view(),name='page-detail')
]

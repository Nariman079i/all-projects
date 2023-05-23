from django.urls import path, include
from .views import *
from rest_framework import routers
from django.views.decorators.cache import cache_page
from .views import *

router = routers.SimpleRouter()



urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/guide/', GuideListView.as_view()),
    path('api/v1/guide/create/', GuideCreateView.as_view()),
    path('api/v1/guide/<int:pk>/', GuideDetailView.as_view()),
    path('api/v1/customer/', CustomerListView.as_view()),
    path('api/v1/customer/create/', CustomerCreateView.as_view()),
    path('api/v1/customer/<int:pk>/', CustomerDetailView.as_view()),
    path('api/v1/services/', ServiceListView.as_view()),
    path('api/v1/services/create/', ServiceCreateView.as_view()),
    path('api/v1/services/<int:pk>/', ServiceDetailView.as_view()),
    path('api/v1/history/', HistoryListView.as_view()),
    path('api/v1/history/create/', HistoryCreateView.as_view()),
    path('api/v1/history/<int:pk>/', HistoryDetailView.as_view())
]

from django.urls import path, include
from .views import *
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'customers', CRMCustomerAPIView)
router.register(r'sessions', CRMSessionAPIView)
router.register(r'masters', CRMMasterAPIView),
router.register(r'services', CRMServiceAPIView)
urlpatterns = [
    path('api/v1/', include(router.urls))

]

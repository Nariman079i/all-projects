from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/',include('items.api.urls')),
    path('api/pages/',include('pages.api.urls')),
    path('api/support/',include('support.api.urls'))

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

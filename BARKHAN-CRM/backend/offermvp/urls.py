
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.conf.urls.static import static


from offermvp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('barkan/', include('barkan.api.urls'))]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
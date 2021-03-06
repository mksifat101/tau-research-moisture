from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from tau_research import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sector/', include('sector.urls')),
    path('', include('dashboard.urls')),
    path('', include('authentication.urls')),
    path('organisation/', include('organisation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

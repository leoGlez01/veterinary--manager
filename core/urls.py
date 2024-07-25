
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Ecop.infraestructure.doctor import urls as doctor_urls
from Ecop.infraestructure.recepcion import urls as recepcion_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', include(doctor_urls)),
    path('recepcion/', include(recepcion_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

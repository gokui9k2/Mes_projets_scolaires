
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('admin', admin.site.urls),
    path('abonnement.html/',abonnement,name="abonnement"),
    path('Lequipe.html/',Lequipe,name="Lequipe"),
    path('support.html/',support,name="support"),
    path('Mdpoublie.html/',Mdpoublie,name="Mdpoublie"),
    path('dashboard.html/',dashboard,name="dashboard"),
    path('solution.html/',solution,name="solution"),
    path('',include('auth_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
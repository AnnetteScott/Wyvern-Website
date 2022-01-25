from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeHub.urls')),
    path('', include('ChemHub.urls')),
    path('', include('GitZak.urls')),
    path('', include('HowToNotDie101.urls')),
    path('', include('NettyHub.urls')),
    path('', include('ToWay.urls')),
    path('', include('CookieBook.urls')),
    path('', include('Arcade.urls')),
    path('', include('WhatToDo.urls')),
    path('', include('Invoice.urls')),
    path('', include('Accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
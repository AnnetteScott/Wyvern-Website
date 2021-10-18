from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeHub.urls')),
    path('', include('ChemHub.urls')),
    path('', include('GitZak.urls')),
    path('', include('HowToNotDie101.urls')),
    path('', include('NettyHub.urls')),
    path('', include('ToWay.urls')),
    path('', include('CookieBook.urls')),
]

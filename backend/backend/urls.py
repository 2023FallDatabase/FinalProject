from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('netflix.urls')),
    path('', include('account.urls')),
    path('', include('social_django.urls', namespace='social')),
]

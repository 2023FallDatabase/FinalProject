from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('netflix.urls')),
    path('', include('account.urls')),
    path('account/', include('social_django.urls', namespace='social')),
    path('comment/', include('message.urls')),
]

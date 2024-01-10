
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('kafka_integration/', include('kafka_integration.urls')),
]

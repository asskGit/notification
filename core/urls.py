
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('celery/', include('django_celery_results.urls')),
    path('', include('app.urls')),


]

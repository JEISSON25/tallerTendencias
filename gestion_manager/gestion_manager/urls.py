from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rol/', include('app.rol.urls')),
    path('api/company/', include('app.company.urls')),
    path('api/accounts/', include('app.accounts.urls')),
]

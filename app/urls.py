from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts.views import register_view
from cars.views import cars_view, new_cars_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register_view, name='register'),
    path('cars/', cars_view, name='cars_list'),
    path('new_car/', new_cars_view, name='new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

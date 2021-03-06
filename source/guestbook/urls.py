from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webapp import views as webapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp_views.index_view, name='index'),
    path('add/', webapp_views.guest_add_view, name='guest-add'),
    path('guest/<int:pk>/', webapp_views.guest_view, name='guest'),
    path('<int:pk>/update', webapp_views.guest_update_view, name='guest-update')
]

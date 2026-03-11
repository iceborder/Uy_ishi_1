from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from root.views import IndexView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

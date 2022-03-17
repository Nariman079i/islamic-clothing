from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

media_url_main = static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )

urlpatterns = [
    path('' , index)
] + media_url_main

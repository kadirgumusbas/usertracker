
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'todos',TodoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls

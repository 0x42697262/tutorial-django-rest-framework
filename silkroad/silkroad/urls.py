from django.contrib         import admin
from django.urls            import path, include
from rest_framework.routers import DefaultRouter

from jobs.views             import JobViewSet
from applications.views     import ApplicationViewSet


router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
# router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('v1/',     include(router.urls)),
]

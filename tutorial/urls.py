from django.conf.urls import include, url, patterns
from django.contrib import admin
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)



urlpatterns = patterns('',
    url(r'^', include('snippets.urls')),
    # url(r'^',include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

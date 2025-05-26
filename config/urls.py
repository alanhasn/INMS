from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from apps.users.views import index_redirect
from django.conf.urls import handler404

# For Deployment
# from users.views import PageNotFound
# handler404 = PageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_redirect , name='index'),
    # path('', IndexRedirectView.as_view() , name="index"),
    
    # Social Auth app
    path('oauth/', include('social_django.urls', namespace='social')),
    # Django Silk url
    path('silk/', include('silk.urls', namespace='silk')),
    #-----------------------------------------------------------------
    path('api/users/', include(('apps.users.urls.api_urls'), namespace='users_api')),
    path('users/', include(('apps.users.urls.ui_urls'))),
    path("reports/",include("apps.reports.urls.ui_urls" , namespace="reports")),
    path("devices/",include("apps.devices.urls.ui_urls" , namespace="devices")),
    path("events/",include("apps.events.urls.ui_urls" , namespace="events")),

]
if settings.DEBUG:  # only for development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
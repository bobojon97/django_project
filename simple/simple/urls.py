from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('test/', include('testapp.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include('simpleApp.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)), 
    ] + urlpatterns

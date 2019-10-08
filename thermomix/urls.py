from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login'), name='go-to-login'),
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
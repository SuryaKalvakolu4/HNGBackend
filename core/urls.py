from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .schema import schema_view


urlpatterns = [
    # swagger urls
    path('swagger(?<format>\\.json|\\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # app urls
    path('admin/', admin.site.urls),
    path('social_auth/', include('social_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('surveys/', include('surveys.urls')),
    path('events/', include('events.urls')),
    path('prizes/', include('prizes.urls')),
    path('challenges/', include('challenges.urls')),
    path('how-it-works/', include('how_it_works.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

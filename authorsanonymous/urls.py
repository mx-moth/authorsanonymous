import wagtail.wagtailadmin.urls
import wagtail.wagtailcore.urls
import wagtail.wagtaildocs.urls
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^robots.txt$', TemplateView.as_view(content_type='text/plain',
                                              template_name='robots.txt')),
    url(r'^admin/', include(wagtail.wagtailadmin.urls)),
    url(r'^documents/', include(wagtail.wagtaildocs.urls)),
    url(r'^contact/$', views.contact_form, name='contact'),

    url(r'', include(wagtail.wagtailcore.urls)),
]


if settings.DEFAULT_FILE_STORAGE == \
        'django.core.files.storage.FileSystemStorage':
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

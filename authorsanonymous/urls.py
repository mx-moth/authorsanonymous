import wagtail.admin.urls
import wagtail.core.urls
import wagtail.documents.urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView
from wagtail.contrib.sitemaps.views import sitemap

from .views import ErrorView, contact_form, contact_submit, newsletter_submit

handler404 = ErrorView.as_view(template_name='layouts/404.html', status=404)
handler500 = ErrorView.as_view(template_name='layouts/500.html', status=500)

urlpatterns = [
    path('robots.txt', TemplateView.as_view(
        content_type='text/plain', template_name='robots.txt')),
    path('sitemap.xml', sitemap),

    path('admin/', include(wagtail.admin.urls)),
    path('documents/', include(wagtail.documents.urls)),
    path('contact/', contact_form, name='contact'),

    path('404/', handler404),
    path('500/', handler500),

    path('_api/contact/',
         contact_submit,
         name='contact_submit'),
    path('_api/newsletter_signup/',
         newsletter_submit,
         name='newsletter_signup'),

    path('', include(wagtail.core.urls)),
]


if settings.DEFAULT_FILE_STORAGE == \
        'django.core.files.storage.FileSystemStorage':
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

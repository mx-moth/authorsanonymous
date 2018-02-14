from textwrap import dedent

from django.db import models
from django.urls import reverse
from django.utils.functional import lazy
from django.utils.html import format_html
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin


def lazy_format_html(value, kwargs_fn):
    return lazy(lambda: format_html(value, **kwargs_fn()), str)()


class Page(MetadataPageMixin, Page):
    body_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, related_name='+', on_delete=models.SET_NULL,
        help_text=lazy_format_html(
            ("Background image for this page. If not set, the background "
             "image in the <a href='{url}'>site copy</a> will be used "
             "instead."),
            lambda: {
                'url': reverse('wagtailsettings:edit', args=('authorsanonymous', 'sitecopy')),
            }))

    settings_panels = Page.settings_panels + [
        ImageChooserPanel('body_background'),
    ]

    class Meta:
        abstract = True

    def get_template(self, request):
        return 'layouts/{}.html'.format(self._meta.model_name)

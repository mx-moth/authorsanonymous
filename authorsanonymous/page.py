from wagtail.wagtailcore.models import Page
from wagtailmetadata.models import MetadataPageMixin


class Page(MetadataPageMixin, Page):
    class Meta:
        abstract = True

    def get_template(self, request):
        return 'layouts/{}.html'.format(self._meta.model_name)

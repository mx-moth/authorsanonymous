from authorsanonymous.page import Page
from wagtail.wagtailcore.fields import StreamField


class FancyPage(Page):
    body = StreamField([])


class ContentPage(Page):
    body = StreamField([])

from django.db import models
from django.utils.html import format_html
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, StreamFieldPanel)
from wagtail.wagtailcore.fields import RichTextField, StreamField

from authorsanonymous.blocks import ContentPageBlocks, FancyPageBlocks
from authorsanonymous.page import Page
from authorsanonymous.utils import FONT_AWESOME_ICONS


class StreamField(StreamField):
    """A streamfield that does not include its blocks in migrations."""
    def deconstruct(self):
        # Drop block_types from args
        name, path, _, kwargs = super(StreamField, self).deconstruct()
        return name, path, [[]], kwargs


class ChoiceField(models.CharField):
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs.pop('choices', None)
        return name, path, args, kwargs


class FancyPage(Page):
    header_icon = ChoiceField(
        "Icon", max_length=40, choices=FONT_AWESOME_ICONS,
        help_text=format_html(
            "See <a href='{}'>Font Awesome</a> for the list of available icons.",
            "http://fontawesome.io/icons/",
        )
    )
    header_text = models.CharField("Title", max_length=255)
    header_body = RichTextField("Text", features=[
        'bold', 'italic', 'link',
    ])

    body = StreamField(FancyPageBlocks())

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('header_icon'),
            FieldPanel('header_text'),
            FieldPanel('header_body'),
        ], "Header"),
        StreamFieldPanel('body'),
    ]


class ContentPage(Page):
    header_text = models.CharField("Title", max_length=255)
    header_body = RichTextField("Text", features=[
        'bold', 'italic', 'link',
    ])

    body = StreamField(ContentPageBlocks())

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('header_text'),
            FieldPanel('header_body'),
        ], "Header"),
        StreamFieldPanel('body'),
    ]


@register_setting
class ContactDetails(BaseSetting):
    email = models.EmailField(blank=True)
    email_public = models.BooleanField(default=False)
    address = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=20)
    facebook_url = models.URLField(blank=True)
    twitter_handle = models.CharField(blank=True, max_length=20)
    instagram_handle = models.CharField(blank=True, max_length=20)

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('email'),
                FieldPanel('email_public'),
            ]),
            FieldPanel('address'),
            FieldPanel('phone'),
            FieldPanel('facebook_url'),
            FieldPanel('twitter_handle'),
            FieldPanel('instagram_handle'),
        ], "Contact details"),
    ]

    @property
    def nice_facebook_url(self):
        if not self.facebook_url:
            return None
        from urllib.parse import urlparse
        bits = urlparse(self.facebook_url)
        return bits.netloc + bits.path

    @property
    def twitter_url(self):
        if not self.twitter_handle:
            return None
        return 'https://twitter.com/{}'.format(self.twitter_handle)

    @property
    def instagram_url(self):
        if not self.instagram_handle:
            return None
        return 'https://instagram.com/{}'.format(self.instagram_handle)


@register_setting
class SiteCopy(BaseSetting):
    site_title = models.CharField(
        max_length=255, blank=False, default="Authors Anonymous",
        help_text="The title shown at the very top of content pages.")
    copyright = models.CharField(
        max_length=255, blank=False, default="Your Name Here",
        help_text="Copyright statement in the footer")

    contact_title = models.CharField(default="Get in touch", max_length=50)
    contact_body = RichTextField()

    panels = [
        FieldPanel('site_title'),
        MultiFieldPanel([
            FieldPanel('contact_title'),
            FieldPanel('contact_body'),
        ], 'Contact form'),
        FieldPanel('copyright'),
    ]

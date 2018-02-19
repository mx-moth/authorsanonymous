from django.utils.html import mark_safe
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HTMLBlock(blocks.TextBlock):
    class Meta:
        icon = 'fa-code'
        label = "Raw HTML"

    def render_basic(self, value, context=None):
        return mark_safe(value)


class FancyFeatureBlock(blocks.StructBlock):
    class ContentBlocks(blocks.StreamBlock):
        text = blocks.RichTextBlock()
        link = blocks.PageChooserBlock()
        html = HTMLBlock()

    title = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    link = blocks.PageChooserBlock(required=False)
    content = ContentBlocks()

    class Meta:
        template = 'blocks/fancy-feature-block.html'


class FancyContentBlock(blocks.StructBlock):
    class ContentBlocks(blocks.StreamBlock):
        text = blocks.RichTextBlock()
        html = HTMLBlock()

    title = blocks.CharBlock()
    content = ContentBlocks()

    class Meta:
        template = 'blocks/fancy-content-block.html'


class FancyPageBlocks(blocks.StreamBlock):
    feature = FancyFeatureBlock()
    content = FancyContentBlock()


class ContentPageBlocks(blocks.StreamBlock):
    text = blocks.RichTextBlock()
    html = HTMLBlock()

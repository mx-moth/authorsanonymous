from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class FancyFeatureBlock(blocks.StructBlock):
    class ContentBlocks(blocks.StreamBlock):
        text = blocks.RichTextBlock()
        link = blocks.PageChooserBlock()

    title = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    link = blocks.PageChooserBlock(required=False)
    content = ContentBlocks()

    class Meta:
        template = 'blocks/fancy-feature-block.html'


class FancyContentBlock(blocks.StructBlock):
    class ContentBlocks(blocks.StreamBlock):
        text = blocks.RichTextBlock()

    title = blocks.CharBlock()
    content = ContentBlocks()


    class Meta:
        template = 'blocks/fancy-content-block.html'


class FancyPageBlocks(blocks.StreamBlock):
    feature = FancyFeatureBlock()
    content = FancyContentBlock()


class ContentPageBlocks(blocks.StreamBlock):
    text = blocks.RichTextBlock()

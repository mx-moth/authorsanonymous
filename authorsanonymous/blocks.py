from functools import total_ordering

from django.template.loader import render_to_string
from django.utils.html import mark_safe
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class StreamBlock(blocks.StreamBlock):
    def render_list_member(self, block_type_name, value, prefix, index, errors=None, id=None):
        """
        Render the HTML for a single list item. This consists of an <li> wrapper, hidden fields
        to manage ID/deleted state/type, delete/reorder buttons, and the child block's own HTML.
        """
        child_block = self.child_blocks[block_type_name]
        child = child_block.bind(value, prefix="%s-value" % prefix, errors=errors)
        return render_to_string('wagtailadmin/block_forms/stream_member.html', {
            'child_blocks': sorted(self.child_blocks.values(), key=lambda child_block: child_block.meta.group),
            'block_type_name': block_type_name,
            'prefix': prefix,
            'child': child,
            'index': index,
            'block_id': id,
        })


@total_ordering
class Group(object):
    """
    Named structblock groups, with sort order
    """

    def __init__(self, order, label):
        self.order = order
        self.label = label

    def __str__(self):
        return self.label

    def __repr__(self):
        return "<Group: %s>" % self.label

    def __lt__(self, other):
        if not isinstance(other, Group):
            return NotImplemented
        return self.order < other.order

    def __eq__(self, other):
        if not isinstance(other, Group):
            return NotImplemented
        return self.order == other.order


CONTENT = Group(100, 'Content')
EMBEDS = Group(200, 'Embeds')


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    align = blocks.ChoiceBlock(choices=[
        ('fit', "Full width"),
        ('left', "Left align"),
        ('right', "Right align"),
    ], default='fit')

    class Meta:
        icon = 'image'
        template = 'blocks/image-block.html'


class HTMLBlock(blocks.TextBlock):
    class Meta:
        icon = 'fa-code'
        label = "Raw HTML"

    def render_basic(self, value, context=None):
        return mark_safe(value)


class ContentBlocks(StreamBlock):
    text = blocks.RichTextBlock(group=CONTENT)
    image = ImageBlock(group=CONTENT)

    html = HTMLBlock(group=EMBEDS)
    embed = EmbedBlock(group=EMBEDS)


class FancyFeatureBlock(blocks.StructBlock):
    class FancyFeatureContentBlocks(ContentBlocks):
        image = None
        link = blocks.PageChooserBlock(group=CONTENT)

    title = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    link = blocks.PageChooserBlock(required=False)
    content = FancyFeatureContentBlocks()

    class Meta:
        template = 'blocks/fancy-feature-block.html'


class FancyContentBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    content = ContentBlocks()

    class Meta:
        template = 'blocks/fancy-content-block.html'


class FancyPageBlocks(StreamBlock):
    feature = FancyFeatureBlock()
    content = FancyContentBlock()


class ContentPageBlocks(ContentBlocks):
    pass

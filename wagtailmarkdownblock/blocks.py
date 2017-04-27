from django.forms import Media
from django.utils.safestring import mark_safe

from markdown import markdown
from wagtail.wagtailcore.blocks import StructBlock, TextBlock


class MarkdownBlock(StructBlock):
    """
    Markdown Block
    """

    markdown = TextBlock()

    @property
    def media(self):
        showdown_version = "1.6.4"

        return Media(
            js=[
                'https://cdnjs.cloudflare.com/ajax/libs/showdown/{}/showdown.min.js'.format(
                    showdown_version,
                ),
            ],
            css={
                "all": ('wagtailmarkdownblock/wagtailmarkdownblock.min.css',),
            }
        )

    def render(self, value, context=None):
        md = markdown(
            value['markdown'],
            [
                'markdown.extensions.fenced_code',
                'codehilite',
            ],
        )
        return mark_safe(md)

    class Meta:
        icon = 'code'
        form_classname = 'markdown-block struct-block'
        form_template = 'wagtailmarkdownblock/markdown_block_form.html'

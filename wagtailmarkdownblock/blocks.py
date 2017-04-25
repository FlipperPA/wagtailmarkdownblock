from django.forms import Media
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

    class Meta:
        icon = 'code'
        template = 'wagtailmarkdownblock/markdown_block.html'
        form_classname = 'markdown-block struct-block'
        form_template = 'wagtailmarkdownblock/markdown_block_form.html'

from django.forms import Media
from django.utils.safestring import mark_safe

import bleach
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
        formatted_html = markdown(
            value['markdown'],
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.nl2br',
                'markdown.extensions.sane_lists',
                'markdown.extensions.toc',
                'markdown.extensions.wikilinks'
            ],
            output_format='html5'
        )

        # Sanitizing html with bleach to avoid code injection
        sanitized_html = bleach.clean(
            formatted_html,
            # Allowed tags, attributes and styles
            tags=[
                'p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'tt', 'pre', 'em', 'strong', 'ul', 'li',
                'dl', 'dd', 'dt', 'code', 'img', 'a', 'table', 'tr', 'th', 'td', 'tbody', 'caption', 'colgroup',
                'thead', 'tfoot', 'blockquote', 'ol', 'hr', 'br'
            ],
            attributes={
                '*': ['class', 'style', 'id'],
                'a': ['href', 'target', 'rel'],
                'img': ['src', 'alt'],
                'tr': ['rowspan', 'colspan'],
                'td': ['rowspan', 'colspan', 'align']
            },
            styles=[
                'color', 'background-color', 'font-family', 'font-weight', 'font-size', 'width', 'height',
                'text-align', 'border', 'border-top', 'border-bottom', 'border-left', 'border-right', 'padding',
                'padding-top', 'padding-bottom', 'padding-left', 'padding-right', 'margin', 'margin-top',
                'margin-bottom', 'margin-left', 'margin-right'
            ]
        )

        return mark_safe(sanitized_html)

    class Meta:
        icon = 'code'
        form_classname = 'markdown-block struct-block'
        form_template = 'wagtailmarkdownblock/markdown_block_form.html'

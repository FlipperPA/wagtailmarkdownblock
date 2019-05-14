from django.utils.safestring import mark_safe

from bleach import clean as bleach_clean
from markdown import markdown


def render(text):

    formatted_html = markdown(
        text,
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            "markdown.extensions.nl2br",
            "markdown.extensions.sane_lists",
            "markdown.extensions.toc",
            "markdown.extensions.wikilinks",
        ],
        output_format="html5",
    )

    # Sanitizing html with bleach to avoid code injection
    sanitized_html = bleach_clean(
        formatted_html,
        # Allowed tags, attributes and styles
        tags=[
            "p",
            "div",
            "span",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "tt",
            "pre",
            "em",
            "strong",
            "ul",
            "li",
            "dl",
            "dd",
            "dt",
            "code",
            "img",
            "a",
            "table",
            "tr",
            "th",
            "td",
            "tbody",
            "caption",
            "colgroup",
            "thead",
            "tfoot",
            "blockquote",
            "ol",
            "hr",
            "br",
            "sub",
            "sup",
        ],
        attributes={
            "*": ["class", "style", "id"],
            "a": ["href", "target", "rel"],
            "img": ["src", "alt"],
            "tr": ["rowspan", "colspan"],
            "td": ["rowspan", "colspan", "align"],
        },
        styles=[
            "color",
            "background-color",
            "font-family",
            "font-weight",
            "font-size",
            "width",
            "height",
            "text-align",
            "border",
            "border-top",
            "border-bottom",
            "border-left",
            "border-right",
            "padding",
            "padding-top",
            "padding-bottom",
            "padding-left",
            "padding-right",
            "margin",
            "margin-top",
            "margin-bottom",
            "margin-left",
            "margin-right",
        ],
    )

    return mark_safe(sanitized_html)

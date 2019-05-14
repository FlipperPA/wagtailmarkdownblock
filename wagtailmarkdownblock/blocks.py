from django import forms
from django.forms import Media
from django.utils.functional import cached_property

try:
    # Wagtail 2
    from wagtail.core.blocks import TextBlock
except ImportError:
    # Wagtail 1
    from wagtail.wagtailcore.blocks import TextBlock


from .widgets import MarkdownTextarea
from .utils import render


class MarkdownBlock(TextBlock):
    """
    Markdown block using SimpleMDE plugin
    """

    def __init__(self, **kwargs):
        if "classname" in kwargs:
            kwargs["classname"] += " markdown"
        else:
            kwargs["classname"] = "markdown"
        super(MarkdownBlock, self).__init__(**kwargs)

    @cached_property
    def field(self):
        field_kwargs = {"widget": MarkdownTextarea()}
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

    @property
    def media(self):
        return Media(
            js=[
                "plugins/simplemde/simplemde.min.js",
                "plugins/simplemde/simplemde.attach.js",
            ],
            css={"all": ("plugins/simplemde/simplemde.min.css",)},
        )

    def render_basic(self, value, context=None):
        return render(value)

    class Meta:
        icon = "code"

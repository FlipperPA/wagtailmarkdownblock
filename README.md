# Wagtail Markdown Block

Markdown blocks for Wagtail Streamfields that display HTML output in realtime in the Wagtail CMS editor.

This Django app uses the [ShowdownJS](https://github.com/showdownjs/showdown) library both in Wagtail Admin and the website and requires jQuery.

## Example Usage

    from wagtailmarkdownblock.blocks import MarkdownBlock

    class ContentStreamBlock(StreamBlock):
        paragraph = RichTextBlock()
        heading = TextBlock()
        code = MarkdownBlock()

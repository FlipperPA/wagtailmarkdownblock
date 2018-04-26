# Wagtail Markdown Block

**PLEASE NOTE:** Future development on this package will be limited, since most of the features are now included in the new Draftail editor available in Wagtail. Thank you to everyone who contributed!

Markdown blocks for Wagtail Streamfields.

This Django app uses the [SimpleMDE](https://simplemde.com/) Markdown editor in the Wagtail Admin and the website.

## Example Usage

    from wagtailmarkdownblock.blocks import MarkdownBlock

    class ContentStreamBlock(StreamBlock):
        paragraph = RichTextBlock()
        heading = TextBlock()
        code = MarkdownBlock()

## Contributors

* Timothy Allen (https://github.com/FlipperPA)
* Milton Lenis (https://github.com/MiltonLn)
* Mathias Picker (https://github.com/mathiasp)
* Tobias Ernst (https://github.com/to-bee)

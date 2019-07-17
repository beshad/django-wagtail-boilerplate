from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel, FieldRowPanel
from wagtail.core.fields import RichTextField, StreamField

from modelcluster.fields import ParentalKey

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

class AboutPage(Page):

    class ImageBlock(blocks.StructBlock):
        image = ImageChooserBlock(required=True)
        caption = blocks.CharBlock(required=False)
        class Meta:
            icon = 'image'

    templates = 'about/about_page.html'
    header = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    date = models.DateField("Selected Date")
    cover = models.TextField(max_length=100, blank=True, null=True)
    left = models.CharField(max_length=100, blank=True, null=True)
    right = models.CharField(max_length=100, blank=True, null=True)
    main = models.CharField(max_length=100, blank=True, null=True, help_text="Some very useful text")

    selection = StreamField([
        ('heading', blocks.CharBlock(label="Some cool heading")),
        ('structblock', ImageBlock()),
        ('number', blocks.IntegerBlock()),
        ('Choice', blocks.ChoiceBlock(choices=[
            ('tea', 'Tea'),
            ('coffee', 'Coffee'),
        ], icon='cup')),
        ('document', DocumentChooserBlock()),
        ('url', blocks.URLBlock()),
        ('date', blocks.DateBlock()),
        ('time', blocks.TimeBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('selection'),
        FieldPanel('header'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('left', classname="col6"),
                FieldPanel('right', classname="col6"),
            ]),
            FieldPanel('main', classname="col12"),
        ], heading="Example of field row"),
        MultiFieldPanel(
        [
            FieldPanel('date'),
            FieldPanel('cover')
        ],
        heading="Collection of Some Fields",
        classname="collapsible collapsed"
    ),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"

    class HomePageGalleryImage(Orderable):
        page = ParentalKey('AboutPage', on_delete=models.CASCADE,
                           related_name='gallery_images')
        image = models.ForeignKey(
            'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
        )
        caption = models.CharField(blank=True, max_length=250)

        panels = [
            ImageChooserPanel('image'),
            FieldPanel('caption'),
        ]

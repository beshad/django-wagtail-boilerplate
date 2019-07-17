from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField

from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalManyToManyField
from wagtail.snippets.models import register_snippet

from pycms.base.blocks import BaseStreamBlock, AlternativeStreamBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
@register_snippet
class Country(models.Model):
    models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "List of Countries"


class HomePage(Page):

    templates = 'home/home_page.html'
    header = models.CharField(max_length=100, blank=True, null=True)
    # body = RichTextField(blank=True, null=True)
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    text = StreamField(
        AlternativeStreamBlock(), verbose_name="Text Body", blank=True
    )

    basic_stream_example = StreamField([
        ('heading', blocks.CharBlock(classname="full title",help_text='super helpful text')),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ],blank=True, null=True, verbose_name="Basic Stream Example")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('basic_stream_example'),
        FieldPanel('header'),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
        StreamFieldPanel('text')
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


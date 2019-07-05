from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField

from modelcluster.fields import ParentalKey

from wagtail.images.edit_handlers import ImageChooserPanel


class AboutPage(Page):

    templates = 'about/about_page.html'
    header = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images")
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

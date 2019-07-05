from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):

    templates = 'home/home_page.html'
    header = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True, null=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('body'),
        ImageChooserPanel('image')
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


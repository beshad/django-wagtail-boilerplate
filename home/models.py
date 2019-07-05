from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField


class HomePage(Page):

    templates = 'home/home_page.html'
    header = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('body')
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

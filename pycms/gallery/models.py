from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    ObjectList,
    TabbedInterface,
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    InlinePanel,
    FieldRowPanel
)

# @register_snippet
class SectionOne(models.Model):
    header = models.CharField(blank=True, null=True,max_length=255)
    body = models.CharField(blank=True, null=True,max_length=255)

    panels = [
        FieldPanel('header'),
        FieldPanel('body'),
    ]

    class Meta:
        abstract = True

# @register_snippet
class SectionTwo(models.Model):
    header = models.CharField(blank=True, null=True,max_length=50)
    body = models.CharField(blank=True, null=True,max_length=80)

    panels = [
        FieldPanel("header"),
        FieldPanel("body")
    ]

    class Meta:
        abstract = True


class GalleryPageSections(Orderable, SectionOne):
    page = ParentalKey('gallery.GalleryPage', on_delete=models.CASCADE, related_name='section_one')

class GalleryPage(Page):

    # section_one = models.ForeignKey(
    #     'SectionOne',
    #     on_delete=models.SET_NULL,
    #     unique=True,
    #     blank=False,
    #     null=True
    # )

    # section_two = models.ForeignKey(
    #     'SectionTwo',
    #     on_delete=models.SET_NULL,
    #     unique=True,
    #     blank=False,
    #     null=True
    # )

    content_panels = [
      InlinePanel('section_one', label="Sections")
      # SnippetChooserPanel('section_one'),
      # SnippetChooserPanel('section_two')
      # InlinePanel('section_one', label="Section One"),
      # InlinePanel('section_two', label="Section Two")
    ]

# @register_snippet
class SectionOne(models.Model):
    header = models.CharField(blank=True, null=True,max_length=255)
    body = models.CharField(blank=True, null=True,max_length=255)

    panels = [
        FieldPanel('header'),
        FieldPanel('body'),
    ]

    class Meta:
        abstract = True



# @register_snippet
class SectionTwo(models.Model):
    header = models.CharField(blank=True, null=True,max_length=50)
    body = models.CharField(blank=True, null=True,max_length=80)

    panels = [
        FieldPanel("header"),
        FieldPanel("body")
    ]

    class Meta:
        abstract = True

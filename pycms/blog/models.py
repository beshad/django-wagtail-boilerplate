from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    ObjectList, 
    TabbedInterface,   
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    InlinePanel
)

class BlogPage(Page):

  text = models.CharField(max_length=100, blank=False, null=True)

  head = models.CharField(max_length=100, blank=False, null=True)
  body = models.CharField(max_length=100, blank=False, null=True)

  # promote_panels=[]
  # settings_panels=[]

  content_panels = Page.content_panels + [
    FieldPanel("text")
  ]

  another_panels = [
        MultiFieldPanel(
            [
                FieldPanel("head"),
                FieldPanel("body"),
            ],
            heading="Another Panel Options",
        ),
    ]
  
       

  edit_handler = TabbedInterface(
    [
      ObjectList(content_panels, heading='Custom'),
      ObjectList(Page.promote_panels, heading='Promotional Stuff'),
      ObjectList(Page.settings_panels, heading='Settings Stuff'),
      ObjectList(another_panels, heading='Another Tab')
    ]
  )

  class Meta:
      verbose_name = "Blog Page"
      verbose_name_plural = "Blog Pages"
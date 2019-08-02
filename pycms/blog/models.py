from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet

from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import (
    ObjectList, 
    TabbedInterface,   
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    InlinePanel,
    FieldRowPanel
)

class BlogAuthor(models.Model):
  name=models.CharField(max_length=50)

  panels = [
    MultiFieldPanel(
      [
        FieldPanel("name")
      ],
      heading="Name Example"
    )
  ]

  def __str__(self):
      return self.name


class BlogPage(Page):

  template= 'blog/blog_page.html'

  text = models.CharField(max_length=100, blank=False, null=True)

  head = models.CharField(max_length=100, blank=False, null=True)
  body = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
  )
  logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
  open_in_new_tab = models.BooleanField(default=False, blank=True, verbose_name="Example")

  banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

  # promote_panels=[]
  # settings_panels=[]

  content_panels = Page.content_panels + [
    FieldPanel("text"),
    InlinePanel('first_section', label="First Section"),
    ImageChooserPanel("banner_image")
  ]

  another_panels = [
        ImageChooserPanel('logo'),
        FieldPanel("open_in_new_tab"),
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

  def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["authors"] = BlogAuthor.objects.all()
        return context

  class Meta:
      verbose_name = "Blog Page"
      verbose_name_plural = "Blog Pages"


class FirstSection(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='first_section')
    header = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)

    panels = [
        FieldPanel('header'),
        FieldPanel('body'),
    ]


register_snippet(BlogAuthor)
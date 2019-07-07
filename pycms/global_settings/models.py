from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSetting(BaseSetting):

  linkedin = models.URLField(blank=True, max_length=50, help_text="Enter LinkedIn URL")
  twitter = models.URLField(blank=True, max_length=50, help_text="Enter Facebook URL")

  panels = [
    MultiFieldPanel([
      FieldPanel("linkedin"),
      FieldPanel("twitter")
    ], heading="Social Media Settings")
  ]
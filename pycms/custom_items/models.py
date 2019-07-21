from django.db import models


class CustomMenuItems(models.Model):

    email = models.CharField(max_length=100, blank=False, null=False, help_text='Email address')
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text='First and last name')

    def __str__(self):
        return self.full_name

    class Meta:  # noqa
        verbose_name = "Custom Menu Item"
        verbose_name_plural = "Custom Menu Items"
from django.db import models
from django.utils.translation import gettext_lazy as _



class ProfileTypeField(models.Model):
    profile_type = models.ForeignKey('ProfileType', on_delete=models.CASCADE)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    required = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.profile_type} - {self.field}'

    class Meta:
        verbose_name = _('Profile Type Field')
        verbose_name_plural = _('Profile Type Fields')
        ordering = ['profile_type']

class Field(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Field')
        verbose_name_plural = _('Fields')
        ordering = ['name']

class ProfileType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    fields = models.ManyToManyField('Field', through='ProfileTypeField')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Profile Type')
        verbose_name_plural = _('Profile Types')
        ordering = ['name']
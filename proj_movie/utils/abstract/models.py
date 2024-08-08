from django.db import models
from django.utils.translation import gettext_lazy as _


class DateTime(models.Model):
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated On"), auto_now=True)

    class Meta:
        abstract = True
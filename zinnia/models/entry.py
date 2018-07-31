"""Entry model for Zinnia"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from zinnia.settings import ENTRY_BASE_MODEL
from zinnia.models_bases import load_model_class


class CanonicalLinkEntry(models.Model):
    """
    Abstract model class providing a lead content to the entries.
    """
    canonical_link = models.URLField(
        _('canonical_link'), blank=True,
        help_text=_("Link to canonical blog post"))

    class Meta:
        abstract = True


class Entry(load_model_class(ENTRY_BASE_MODEL), CanonicalLinkEntry):
    """
    The final Entry model based on inheritence.
    """

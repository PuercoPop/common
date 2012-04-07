# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from common.middleware import threadlocals
from common.utils import to32
from django.utils.translation import ugettext as _

class AuditableManager(models.Manager):
    """
    Replacement for the default manager in AuditableModels so we only query
    for the active objects.
    """
    pass

class AuditableModel(models.Model):
    """
    AuditableModel inherits from models.Model and implements the following
    fields for audit purposes:
      * url_id
      * created
      * modified
      * created_by
      * modified_by
    """

    url_id = models.CharField(max_length=16, blank=True, editable=False)
    created = models.DateTimeField(verbose_name=_('Creado'),
                    auto_now_add=True,
                    editable=False)
    modified = models.DateTimeField(verbose_name=_('Modificado'),
                    auto_now=True,
                    null=True,
                    editable=False)
    created_by = models.ForeignKey(User, verbose_name=_('Creado por'),
                    related_name="%(class)s_related",
                    editable=False)
    modified_by = models.ForeignKey(User, verbose_name=_('Modificado por'),
                    related_name="%(class)s_related_mod",
                    null=True,
                    editable=False)

    def save(self, *args, **kwargs):
        """
        If its a new object, set the creation user and assign the url_id
        """
        # If the object already existed, it will already have an id
        if self.id:
            user = threadlocals.get_non_anonymous_user()
            if user.is_staff and hasattr(self,"admined") and \
              hasattr(self,"admined_by"):
                # This object is being edited by an admin set the admined
                self.admined_by = threadlocals.get_non_anonymous_user()
                self.admined = datetime.now()
            else:
                # This object is being edited, not saved, set last_edited_by
                self.modified_by = threadlocals.get_non_anonymous_user()
        else:
            # This is a new object, set the owner
            self.created_by = threadlocals.get_non_anonymous_user()
            # Save first to obtain an ID
            super(AuditableModel, self).save(*args, **kwargs)
            kwargs['force_insert'] = False

        # Check is url_id exist, if not, generate to save
        if not self.url_id:
            self.url_id = to32(self.id) # Set real value

        super(AuditableModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

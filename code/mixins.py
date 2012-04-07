# -*- coding: utf-8 -*-

from django.conf import settings

class ObjectWithPictureMixin(object):

    def get_picture_url(self):
        """
        Returns the fully qualified URL to the picture
        of the model object as an asset available as a 
        thumbnail that gets dinamically created with the 
        requested dimensions.
        """
        if self.picture:
            return "%s%s" % (
                settings.ASSETS_PREFIX,
                self.picture.url.replace(settings.ASSETS_PATH_TO_REMOVE, '')
            )
        else:
            return None

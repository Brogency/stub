# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer


class ImageThumbnailMixin(models.Model):
    IMAGE_EXTENSIONS = [
        "JPG", "JPEG", "TIFF", "TIF",
        "R3D", "ARI", "GIF", "BMP", "PNG",
    ]

    class Meta:
        abstract = True

    def image_tag(self):
        if self.pk is None:
            return ""  # May be empty inline.

        if not hasattr(self, "ext") or not hasattr(self, "doc"):
            raise Exception("Property ext or doc is not defined")

        if self.ext not in self.IMAGE_EXTENSIONS:
            return ""

        options = {"size": (100, 100), "crop": True}

        try:
            thumb_url = get_thumbnailer(self.doc) \
                .get_thumbnail(options).url
        except InvalidImageFormatError:
            return ""

        return "<img src='{path}'/>".format(path=thumb_url)

    image_tag.short_description = _("Image")
    image_tag.allow_tags = True

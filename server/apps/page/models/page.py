# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codemirror import CodeMirrorTextarea
from django.contrib.contenttypes.generic import GenericRelation
from django.contrib.flatpages.models import FlatPage
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.db import models
from funcy import first
from redactor.widgets import RedactorEditor

from apps.filestorage.models.filestorage import RelativeFileStorage, FileStorage
from apps.filestorage.models.mixins.image import ImageThumbnailMixin


class EditorTypesEnum(object):

    # Tuple of available editors type. First element: editor class,
    # second options for this instance

    EDITOR_TYPES = (
        (RedactorEditor, {},),
        (CodeMirrorTextarea, {'dependencies': ("xml", "javascript", "css")}),
    )

    @classmethod
    def get_choices(cls):
        """Generate choices from EDITOR_TYPES"""
        return ((i, first(e).__name__)
                for i, e in enumerate(cls.EDITOR_TYPES))

    @classmethod
    def get_editor(cls, editor_id):
        """Getting editor by `editor_id`. Param editor_id is index in tuple
        from method cls.get_choices()

        Usage:

        >>> EditorTypesEnum.get_editor(editor_id=0)
        (<class 'redactor.widgets.RedactorEditor'>, {})

        :param editor_id: int
        :return: tuple
        """
        return first(
            (e for i, e in enumerate(cls.EDITOR_TYPES) if i == editor_id))


# add additional field document_set
FlatPage.add_to_class(
    'document_set', GenericRelation(FileStorage)
)

# add additional field type_editor
FlatPage.add_to_class(
    'type_editor', models.IntegerField(
        verbose_name=_("Editor_type"),
        default=0,
        choices=EditorTypesEnum.get_choices())
)

# add additional field file_set
FlatPage.add_to_class(
    'file_set', GenericRelation(RelativeFileStorage)
)

# add field IMAGE_EXTENSIONS
FlatPage.add_to_class(
    'IMAGE_EXTENSIONS',
    ImageThumbnailMixin.IMAGE_EXTENSIONS
)


def get_documents(self):
    return self.file_set \
        .exclude(document__extension__in=self.IMAGE_EXTENSIONS) \
        .filter(languages__contains=translation.get_language())


def get_images(self):
    return self.file_set \
        .filter(document__extension__in=self.IMAGE_EXTENSIONS) \
        .filter(languages__contains=translation.get_language())


FlatPage.add_to_class(
    'get_documents',
    get_documents
)

FlatPage.add_to_class(
    'get_images',
    get_documents
)

FlatPage.add_to_class(
    'header_text',
    models.TextField(
        verbose_name="Header text",
        blank=True,
        null=True
    )
)

# AUDIT LOG

from django.contrib.admin.models import ACTION_FLAG_CHOICES
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _

ADDITION = 1
CHANGE = 2
DELETION = 3


class AuditLogBase(models.Model):
    """
    An abstract base model class for auditing actions.

    This model provides fields to track audit log information,
    including:

    - `action_time`: The timestamp of the action.
    - `object_id`: The ID of the object related to the action.
    - `object_repr`: A string representation of the object.
    - `action_flag`: The flag indicating the type of action performed.
    - `user_id`: The ID of the user associated with the action.
    - `organization_id`: The ID of the organization associated with the
        action.
    - `change_message`: A JSON field to store additional change
        information.
    - `component_type`: The type of component related to the action.

    Meta:
        abstract (bool): Specifies that this model is abstract and
        cannot be instantiated.

    Attributes:
        action_time (DateTimeField): The timestamp of the action.
        object_id (TextField): The ID of the object related to the action.
        object_repr (CharField): A string representation of the object.
        action_flag (PositiveSmallIntegerField): The flag indicating the
            type of action performed.
        user_id (IntegerField): The ID of the user associated with the
            action.
        organization_id (IntegerField): The ID of the organization
            associated with the action.
        change_message (JSONField): A JSON field to store additional
            change information.
        component_type (SmallIntegerField): The type of component
            related to the action.

    Methods:
        __repr__(self): Returns a string representation of
        the action time.

    Example:
        ```python
        class MyAuditLog(AuditLogBase):
            # ...
        ```
    """

    action_time = models.DateTimeField(
        _("action time"),
        auto_now_add=True,
        editable=False,
    )
    object_id = models.TextField(_("object id"), blank=True, null=True)
    object_repr = models.CharField(_("object repr"), max_length=200)
    action_flag = models.PositiveSmallIntegerField(
        _("action flag"),
        choices=ACTION_FLAG_CHOICES,
        db_index=True,
    )
    # project fields
    user_id = models.IntegerField(db_index=True, blank=True, null=True)
    organization_id = models.IntegerField(db_index=True, blank=True, null=True)
    change_message = models.JSONField(null=True, blank=True)
    component_type = models.SmallIntegerField(
        verbose_name="ComponentType",
        help_text=("Ex: 1.BASIC, 2.CONFIG, 3.MODULE, 4.VIDEO_LECTURE",),
        validators=[MinValueValidator(1)],
    )

    class Meta:
        abstract = True

    def __repr__(self):
        return smart_str(self.action_time)

    def is_addition(self):
        return self.action_flag == ADDITION

    def is_change(self):
        return self.action_flag == CHANGE

    def is_deletion(self):
        return self.action_flag == DELETION

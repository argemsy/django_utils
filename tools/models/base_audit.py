from django.db import models


class AuditBase(models.Model):
    """
    An abstract base model class for auditing purposes.

    This model provides common fields for auditing, including:
    - `created_at`: The timestamp of creation.
    - `updated_at`: The timestamp of the last update.
    - `is_active`: A flag indicating if the object is active.
    - `is_deleted`: A flag indicating if the object is deleted.

    Meta:
        abstract (bool): Specifies that this model is abstract and
        cannot be instantiated.

    Attributes:
        created_at (DateTimeField): The timestamp of creation.
        updated_at (DateTimeField): The timestamp of the last update.
        is_active (BooleanField): A flag indicating if the object is
            active.
        is_deleted (BooleanField): A flag indicating if the object is
            deleted.

    Example:
        ```python
        class MyModel(AuditBase):
            name = models.CharField(max_length=100)
            # ...
        ```
    """

    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, editable=False, null=True
    )
    update_at = models.DateTimeField(
        auto_now=True, db_index=True, null=True, editable=False
    )
    is_active = models.BooleanField(
        default=True,
        db_index=True,
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

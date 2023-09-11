# Third-party Libraries
from django.contrib import admin, messages
from django.utils import timezone


class AdminMixin(admin.ModelAdmin):
    """
    A mixin class for admin models that provides additional actions.

    This mixin class adds the following actions to the admin interface:
    - Logical deletion: Marks selected objects as deleted.
    - Logical restoration: Marks selected objects as not deleted.
    - Activation: Activates selected objects.
    - Deactivation: Deactivates selected objects.

    Attributes:
        date_hierarchy (str): The name of the field used for date-based
            hierarchy navigation.
        actions (list): The list of additional actions available in the
            admin interface.

    Methods:
        logical_deletion(self, request, queryset): Marks selected
            objects as deleted.
        logical_restoration(self, request, queryset): Marks selected
            objects as not deleted.
        activation(self, request, queryset): Activates selected objects.
        deactivation(self, request, queryset): Deactivates selected
            objects.
    """

    date_hierarchy = "created_at"
    actions = [
        "logical_deletion",
        "logical_restoration",
        "activation",
        "deactivation",
    ]

    @admin.display(description="Logical deletion")
    def logical_deletion(self, request, queryset):
        """
        Displays the logical deletion action in the admin interface.

        This action marks the selected objects in the queryset as
        deleted by updating their `is_deleted` field to `True` and
        setting the `updated_at` field to the current time. It also
        displays a success message to the user.

        Args:
            self: The instance of the admin class.
            request: The current request object.
            queryset: The queryset containing the selected objects.

        Returns:
            The updated queryset.

        """
        model = self.model._meta.verbose_name
        n = queryset.count()
        message = f"{n} {model} han sido marcados como eliminados." % {
            "count": n,
            "model": model,
        }
        self.message_user(request, message, messages.SUCCESS)
        queryset.update(is_deleted=True, updated_at=timezone.now())
        return queryset

    @admin.display(description="Logical restoration")
    def logical_restoration(self, request, queryset):
        """
        Displays the logical restoration action in the admin interface.

        This action marks the selected objects in the queryset as not
        deleted by updating their `is_deleted` field to `False` and
        setting the `updated_at` field to the current time. It also
        displays a success message to the user.

        Args:
            self: The instance of the admin class.
            request: The current request object.
            queryset: The queryset containing the selected objects.

        Returns:
            The updated queryset.

        """
        model = self.model._meta.verbose_name
        n = queryset.count()
        message = f"{n} {model} han sido desmarcados como eliminados."
        self.message_user(request, message, messages.SUCCESS)
        queryset.update(is_deleted=False, updated_at=timezone.now())
        return queryset

    @admin.display(description="Activation")
    def activation(self, request, queryset):
        """
        Displays the activation action in the admin interface.

        This action activates the selected objects in the queryset,
        updates their `is_active` field to `True`, and sets the
        `updated_at` field to the current time. It also displays a
        success message to the user.

        Args:
            self: The instance of the admin class.
            request: The current request object.
            queryset: The queryset containing the selected objects.

        Returns:
            The updated queryset.

        """
        model = self.model._meta.verbose_name
        n = queryset.count()
        message = f"{n} {model} han sido activados." % {
            "count": n,
            "model": model,
        }
        self.message_user(request, message, messages.SUCCESS)
        queryset.update(is_active=True, updated_at=timezone.now())
        return queryset

    @admin.display(description="Deactivation")
    def deactivation(self, request, queryset):
        """
        Displays the deactivation action in the admin interface.

        This action deactivates the selected objects in the queryset,
        updates their `is_active` field to `False`, and sets the
        `updated_at` field to the current time. It also displays a
        success message to the user.

        Args:
            self: The instance of the admin class.
            request: The current request object.
            queryset: The queryset containing the selected objects.

        Returns:
            The updated queryset.
        """
        model = self.model._meta.verbose_name
        n = queryset.count()
        message = f"{n} {model} han sido desactivados." % {
            "count": n,
            "model": model,
        }
        self.message_user(request, message, messages.SUCCESS)
        queryset.update(is_active=False, updated_at=timezone.now())
        return queryset

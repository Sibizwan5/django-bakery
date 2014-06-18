import logging
from django.conf import settings
from django.core import management
logger = logging.getLogger(__name__)
try:
    from celery.task import task
    from celery.decorators import task
except ImportError:
    raise ImportError("celery must be installed to use django-bakery's tasks")


@task()
def publish_object(obj):
    """
    Build all views related to an object, and then sync with S3.

    Accepts a model object that inherits bakery's BuildableModel class.
    """
    try:
        # Build the object 
        obj.build()
        # Run the `publish` management command unless the
        # ALLOW_BAKERY_PUBLISHING variable is explictly set to False.
        if getattr(settings, 'ALLOW_BAKERY_PUBLISHING', True):
            management.call_command("publish")
    except Exception:
        # Log the error if this crashes
        logger.error("Task Error: publish_object", exc_info=True)


@task()
def unpublish_object(obj):
    """
    Unbuild all views related to a object and then sync to S3.

    Accepts a model object that inherits bakery's BuildableModel class.
    """
    try:
        # Unbuild the object
        obj.unbuild()
        # Run the `publish` management command unless the
        # ALLOW_BAKERY_PUBLISHING variable is explictly set to False.
        if getattr(settings, 'ALLOW_BAKERY_PUBLISHING', True):
            management.call_command("publish")
    except Exception:
        # Log the error if this crashes
        logger.error("Task Error: unpublish_object", exc_info=True)

from core import models


class AuditModelMixin(models.BaseTimestampedModel,
                      models.BaseUserTrackedModel):

    """ 
    Mixin that provides fields created and updated at and by fields

    Includes
        - BaseTimestampedModel 
        - BaseUserTrackedModel
    """
    class Meta:
        abstract = True


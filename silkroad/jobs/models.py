from django.db          import models
from django.contrib.auth.models import User


class Job(models.Models):
    """
    Job Model
    Defines the attributes of a job.
    """
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at      = models.DateTimeField(auto_now_add=True)
    modified_at     = models.DateTimeField(auto_now=True)
    is_deleted      = models.BooleanField()




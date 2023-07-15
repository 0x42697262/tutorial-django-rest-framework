from django.contrib.auth.models     import User
from django.db                      import models


STATUS_CHOICES = (
    (-1, 'Declined'),
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Withdrawn'),
)


class Job(models.Model):
    """
    Job Model
    Defines the attributes of a job.
    """
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    status          = models.IntegerField(choices=STATUS_CHOICES, default=0)
    title           = models.TextField(max_length=32, null=True)
    description     = models.TextField(max_length=256, null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    modified_at     = models.DateTimeField(auto_now=True)
    is_deleted      = models.BooleanField()




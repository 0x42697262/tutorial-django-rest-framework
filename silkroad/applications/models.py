from django.contrib.auth.models     import User
from django.db                      import models
from jobs.models                    import Job


STATUS_CHOICES = (
    (-1, 'Declined'),
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Withdrawn'),
)


class Application(models.Model):
    """
    Application Model
    Defines the attributes of a application.
    """
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    status          = models.IntegerField(choices=STATUS_CHOICES, default=0)
    applied_job     = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    modified_at     = models.DateTimeField(auto_now=True)
    is_deleted      = models.BooleanField()




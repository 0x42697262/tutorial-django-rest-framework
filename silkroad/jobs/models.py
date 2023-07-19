from django.contrib.auth.models     import User
from django.db                      import models



class Job(models.Model):
    """
    Job Model
    Defines the attributes of a job.
    """
    owner           = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.TextField(max_length=32, null=True)
    description     = models.TextField(max_length=256, null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    modified_at     = models.DateTimeField(auto_now=True)
    is_deleted      = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

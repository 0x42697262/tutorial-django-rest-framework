from django.db import models

# Create your models here.


class TestCaseInput(models.Model):
    string_input    = models.CharField(max_length=1000)
    is_valid        = models.BooleanField()

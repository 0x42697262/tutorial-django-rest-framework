from django.db import models
import uuid

# Create your models here.

class TestCases(models.Model):
    regex   = models.CharField(max_length=20, unique=True, default="e")

    def __str__(self):
        return f"{id} -- {self.regex}"

class StringInputs(models.Model):
    case  = models.ForeignKey(
                    TestCases,
                    related_name='case',
                    on_delete=models.CASCADE,
                    )
    string_input = models.CharField(max_length=1000)

    class Meta:
        ordering = ['case']

    def __str__(self):
        return f"{self.string_input}"

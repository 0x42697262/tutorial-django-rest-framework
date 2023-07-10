from django.db import models
import uuid

# Create your models here.

class TestCases(models.Model):
    case_count  = models.IntegerField()
    regex       = models.CharField(max_length=20)

    def __str__(self):
        return f"{id} -- {self.case_count} -- {self.regex}"

class StringInputs(models.Model):
    test_case       = models.ForeignKey("TestCases", on_delete=models.CASCADE)
    string_input    = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.test_case} -- {self.string_input}"

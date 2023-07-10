# Machine Problem Project

## Running

Run `python manage.py runserver`.

## models.py

Adding a new model is easy. First create a class and then the fields of the class.
```python
class SampleTable(models.Model):
    name = models.CharField(max_length=64)
    age  = models.IntegerField()
```

After creating a model, make sure to execute `makemigrations` and `migrate`. You can do this by `python manage.py makemigrations <project name>` and `python manage.py migrate`.


---

# Chapter 1 Machine Problem

## models.py

To add new data to the database, simply run `python manage.py shell` and import the models.

```
from ch1.models import TestCases, StringInputs

TestCases.objects.create(case_count=4, regular_expression='aaabbbbbb')
...
```


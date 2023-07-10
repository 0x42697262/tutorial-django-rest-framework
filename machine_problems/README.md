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

After creating a model, make sure to execute `makemigrations` and `migrate`. You can do this by `python manage.py makemigrations` and `python manage.py migrate`.


---

# Chapter 1 Machine Problem



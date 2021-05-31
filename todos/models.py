from django.db import models


# Create your models here.
class Todos(models.Model):
    task = models.CharField(max_length=200)
    date = models.CharField(max_length=120, null=True)
    stauses=(
        ("complete","complete"),
        ("incomplete","incomplete"),
        ("failed","failed")
    )
    status = models.CharField(max_length=120,choices=stauses)

    def __str__(self):
        return self.task

from django.db import models

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    salary = models.IntegerField(default=25000, blank=False)
    company = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.last_name}  {self.first_name}'

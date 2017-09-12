from django.db import models


def foo(*a, **kw):
    print(a, kw)
    return {}


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    departament = models.ForeignKey('Departament')

    def __str__(self):
        return self.name


class Something(models.Model):
    tltle = models.TextField()


class Departament(models.Model):
    title = models.CharField(max_length=20)
    boss = models.ForeignKey(Person, related_name='xxx', blank=True, null=True)
    something = models.ForeignKey(Something)

    def __str__(self):
        return self.title

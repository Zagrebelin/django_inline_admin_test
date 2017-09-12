from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    departament = models.ForeignKey('Departament')

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Departament(models.Model):
    title = models.CharField(max_length=20)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.title

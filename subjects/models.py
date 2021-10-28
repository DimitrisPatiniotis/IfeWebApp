from django.db import models


class Subject(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    code = models.CharField(blank=True, null=True, max_length=7)
    ects = models.IntegerField(blank=True, null=True)

class OldSubject(models.Model):
    new_subject_match = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=50)
    code = models.CharField(blank=True, null=True, max_length=7)
    ects = models.IntegerField(blank=True, null=True)


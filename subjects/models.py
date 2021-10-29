from django.db import models

class Subject(models.Model):
    name = models.CharField(blank=True, null=True, max_length=58)
    code = models.CharField(blank=True, null=True, max_length=7)
    ects = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.code + ' ' + self.name

class OldSubject(models.Model):
    new_subject_match = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=50)
    code = models.CharField(blank=True, null=True, max_length=7)
    ects = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.code

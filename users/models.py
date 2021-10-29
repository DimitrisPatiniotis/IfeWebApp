from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from subjects.models import Subject, OldSubject

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length = 50, default='NONAME', null=False)
    registration_number  = models.IntegerField(default='0', null=False)
    
    def get_number_of_subjects(self):
        return len(PassedSubjects.objects.filter(user=self))
            
    def __str__(self):
        return self.name

class PassedSubjects(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField(default=5, validators=[MaxValueValidator(10), MinValueValidator(5)])

    def __str__(self):
        return str(self.user) + ' ' + self.subject.name + ' ' + str(self.mark)
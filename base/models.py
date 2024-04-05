from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    note = models.TextField(null = True, blank = True)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['done','-due_date','-due_time','-updated','-created']

    def __str__(self):
        return self.title
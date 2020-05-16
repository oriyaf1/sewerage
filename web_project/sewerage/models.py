from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Controller(models.Model):
    controller_id = models.IntegerField()
    status = models.CharField(max_length=15)
    installed_date = models.DateTimeField(default=timezone.now)
    location = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "id " + str(self.controller_id) + " - " + self.status

    
    def get_absolute_url(self):
        return reverse('controller-detail', kwargs={'pk': self.pk})
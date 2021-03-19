from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateField()

    # show on database blog title
    def __str__(self):
        return self.title

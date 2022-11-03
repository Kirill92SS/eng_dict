from django.db import models


class Dictionary(models.Model):
    words = models.CharField(max_length=255)

    def __str__(self):
        return self.words

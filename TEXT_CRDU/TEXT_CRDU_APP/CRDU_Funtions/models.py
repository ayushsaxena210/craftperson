from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        super(Words, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.word)

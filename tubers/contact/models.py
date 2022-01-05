from django.db import models

# Create your models here.

class Detail(models.Model):
    mail = models.CharField(max_length=255)
    call = models.BigIntegerField()
    fb_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)

    def __str__(self):
        return self.mail

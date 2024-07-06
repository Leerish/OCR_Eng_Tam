# translator/models.py

from django.db import models

class TranslationRequest(models.Model):
    newspaper_name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newspaper_name

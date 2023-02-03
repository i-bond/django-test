from django.db import models

# Create your models here.


class ShortURL(models.Model):
    original_url = models.URLField(max_length=500, unique=True)
    short_url = models.CharField(max_length=6, unique=True)
    times_followed = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'url_shortener'
        ordering = ["-created_at"]

    def __str__(self):
        return self.original_url






























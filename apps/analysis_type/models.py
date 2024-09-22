from django.db import models


class Types(models.Model):
    name = models.CharField(max_length=100)
    ru_name = models.CharField(max_length=100)
    price = models.IntegerField()
    info = models.TextField()
    ru_info = models.TextField()
    to_be_ready = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name

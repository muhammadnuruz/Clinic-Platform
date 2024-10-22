from django.db import models

class Analyses(models.Model):
    analyse_id = models.IntegerField()
    file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Analiz "
        verbose_name_plural = "Analizlar "

    def __str__(self):
        return f"{self.analyse_id}"

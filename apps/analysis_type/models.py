from django.db import models


class Types(models.Model):
    CATEGORY_CHOICES = [
        ('gormon', 'Gormonal tekshiruvlar'),
        ('bioximik', 'Bioximik tekshiruvlar'),
        ('bakteriologik', 'Bakteriologik tekshiruvlar'),
        ('psr', 'PSR tekshiruvlar'),
        ('klinik', 'Klinik laborator tekshiruvlar'),
        ('mikroskopik', 'Mikroskopik tekshiruvlar'),
    ]

    RU_CATEGORY_CHOICES = [
        ('gormon', 'Гормональные исследования'),
        ('bioximik', 'Биохимические исследования'),
        ('bakteriologik', 'Бактериологические исследования'),
        ('psr', 'ПЦР исследования'),
        ('klinik', 'Клинические лабораторные исследования'),
        ('mikroskopik', 'Микроскопические исследования'),
    ]

    name = models.CharField(max_length=100)
    ru_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    ru_category = models.CharField(max_length=100, choices=RU_CATEGORY_CHOICES)
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

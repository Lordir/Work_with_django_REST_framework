from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, blank=True, unique=True, db_index=True, verbose_name="URL")
    price = models.FloatField(max_length=10, verbose_name="Цена")

    def __str__(self):
        return self.name

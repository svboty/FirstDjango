from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __repr__(self):
        return f"Item: {self.name} {self.brand} {self.count}"

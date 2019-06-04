from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256)
    caption = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='category')
    price = models.FloatField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return '{}: {} - {} rub'.format(str(self.id), self.title, str(self.price))


class Category(models.Model):
    title = models.CharField(max_length=256, unique=True)
    path_name = models.SlugField(unique=True, blank=False)
    caption = models.TextField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}'.format(self.title)

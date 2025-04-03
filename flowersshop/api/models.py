from django.db import models


class Flower(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.price)

class Extra(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Добавка'
        verbose_name_plural = 'Добавки'

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.price)

class Bucket(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    flowers = models.ManyToManyField(Flower, verbose_name='Цветы в составе')
    extras = models.ManyToManyField(Extra, verbose_name='Добавки')

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

    def __str__(self):
        return '{0} - Цена: {1}, Кол-во цветков: {2}'.format(self.name, self.price, self.flowers.all().count())



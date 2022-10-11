from django.db import models


class Order(models.Model):
    STATUS = [('New', 'New'),
              ('In Process', 'In Process'),
              ('Stored', 'Stored'),
              ('Send', 'Send')]
    number = models.CharField(max_length=100, verbose_name='Номер заказа')
    status = models.CharField(
        max_length=20, choices=STATUS, default='New', verbose_name='Статуc')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f' Order number {self.number} have status {self.status}'

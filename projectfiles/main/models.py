from django.db import models

class Clothing(models.Model):

    type_cl = models.ForeignKey('Types' , on_delete=models.PROTECT)
    title = models.CharField(verbose_name="Название" , max_length=40 , null=False)
    photo = models.ImageField(verbose_name="Изображение" , upload_to="img/" , null=True )
    color = models.CharField(verbose_name="Цвет ткани" , max_length=40 , null=False)
    price = models.IntegerField(verbose_name="Цена" , default=0)
    on_view_price = models.BooleanField(verbose_name="Отобразить цену" , default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'


class Types(models.Model):
    name = models.CharField(verbose_name="Тип ткани" , max_length=40 , null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

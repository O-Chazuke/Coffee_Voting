from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Roasting(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    brand=models.CharField(max_length=255,verbose_name='豆の名前')
    roasting=models.ForeignKey(
        Roasting,
        on_delete=models.PROTECT,
        verbose_name='焙煎度'
    )
    beans_grams=models.FloatField(verbose_name='豆のグラム数 [g]')
    time=models.IntegerField(verbose_name='抽出時間 [s]')
    temperature=models.FloatField(verbose_name='湯の温度 [℃]')
    final_grams=models.FloatField(verbose_name='最終的な量 [ml]')
    comment=models.TextField(null=True,blank=True,verbose_name='抽出コメント')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand
    
    def get_absolute_url(self):
        return reverse('coffee_voting:detail', kwargs={'pk': self.pk})


class Voting(models.Model):
    bitterness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],verbose_name='苦味')
    sourness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],verbose_name='酸味')
    sweetness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],verbose_name='甘味')
    richness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],verbose_name='コク')
    flavor=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],verbose_name='香り')
    review=models.TextField(max_length=255,null=True,blank=True,verbose_name='レビュー')
    coffee_id=models.ForeignKey(
        Coffee,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.coffee_id)
    
    def get_absolute_url(self):
        return reverse('coffee_voting:index')

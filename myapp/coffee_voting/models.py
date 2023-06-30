from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Roasting(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Coffee(models.Model):
    name=models.CharField(max_length=255)
    roasting=models.ForeignKey(
        Roasting,
        on_delete=models.PROTECT,
    )
    brand=models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        null=True,blank=True
    )
    beans_grams=models.FloatField()
    time=models.IntegerField()
    temperature=models.FloatField()
    final_grams=models.FloatField()
    comment=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('coffee_voting:detail', kwargs={'pk': self.pk})


class Voting(models.Model):
    bitterness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    sourness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    sweetness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    richness=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    flavor=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    review=models.CharField(max_length=255,null=True,blank=True)
    coffee_id=models.ForeignKey(
        Coffee,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.coffee_id)
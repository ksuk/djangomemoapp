from django.db import models
from django.core import validators
# Create your models here.

class Item(models.Model):
    SEX_CHOICE = (
        (1, "Men"),
        (2, "Women"),
    )

    name = models.CharField(verbose_name="Name", max_length=50)

    age = models.IntegerField(verbose_name="Age", validators=[validators.MinLengthValidator(1)], blank=True, null=True)

    sex = models.IntegerField(verbose_name="Sex", choices=SEX_CHOICE, default=1)

    memo = models.TextField(verbose_name="other", max_length=240, blank=True, null=True)

    created_date = models.DateTimeField(verbose_name="Add date", auto_now=False, auto_now_add=True)

    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Item"   
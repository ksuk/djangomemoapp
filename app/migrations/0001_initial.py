# Generated by Django 2.1.4 on 2018-12-12 03:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Age')),
                ('sex', models.IntegerField(choices=[(1, 'Men'), (2, 'Women')], default=1, verbose_name='Sex')),
                ('memo', models.TextField(blank=True, max_length=240, null=True, verbose_name='other')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Add date')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Item',
            },
        ),
    ]

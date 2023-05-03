# Generated by Django 4.1.7 on 2023-05-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_basemodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='URL'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_cassettecategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='basemodel',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='URL'),
        ),
    ]

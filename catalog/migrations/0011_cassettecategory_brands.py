# Generated by Django 4.1.7 on 2023-05-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_basemodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cassettecategory',
            name='brands',
            field=models.ManyToManyField(blank=True, to='catalog.cassettebrand', verbose_name='Brands'),
        ),
    ]

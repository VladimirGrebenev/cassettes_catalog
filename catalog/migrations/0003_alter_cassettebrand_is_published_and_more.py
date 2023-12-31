# Generated by Django 4.1.7 on 2023-10-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cassettebrand',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='cassettecollection',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='cassettemanufacturer',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='cassettemodel',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='cassetteseries',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='cassettetechnology',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='cassettetype',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
    ]

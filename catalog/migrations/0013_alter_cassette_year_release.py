# Generated by Django 4.1.7 on 2023-05-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_cassette_year_release_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cassette',
            name='year_release',
            field=models.IntegerField(verbose_name='Year Release'),
        ),
    ]

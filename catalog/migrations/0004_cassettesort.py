# Generated by Django 4.1.7 on 2023-10-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_cassettebrand_is_published_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CassetteSort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='title')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Url/Slug')),
                ('is_published', models.BooleanField(default=True, verbose_name='Publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date of updated')),
            ],
            options={
                'verbose_name': 'sort',
                'verbose_name_plural': 'sorts',
            },
        ),
    ]

# Generated by Django 3.0.5 on 2020-08-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0020_auto_20200811_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vector',
            name='dnas',
            field=models.ManyToManyField(blank=True, related_name='vectors', to='registry.Dna'),
        ),
    ]

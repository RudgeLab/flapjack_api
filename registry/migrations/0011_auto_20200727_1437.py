# Generated by Django 3.0.5 on 2020-07-27 14:37

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registry', '0010_auto_20200727_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dna',
            name='sboluris',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='study',
            name='shared_with',
            field=models.ManyToManyField(blank=True, default=list, related_name='shared_studies', to=settings.AUTH_USER_MODEL),
        ),
    ]

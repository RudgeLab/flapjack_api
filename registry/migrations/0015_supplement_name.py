# Generated by Django 3.0.5 on 2020-07-31 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0014_vector_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplement',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

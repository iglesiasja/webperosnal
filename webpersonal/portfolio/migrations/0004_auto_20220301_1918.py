# Generated by Django 2.0.2 on 2022-03-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20220301_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion Web'),
        ),
    ]

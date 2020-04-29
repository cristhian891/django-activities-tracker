# Generated by Django 3.0.4 on 2020-04-16 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20200415_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='calories',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='distance',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='sport',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 2.0.2 on 2018-02-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='melon_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='멜론 Album ID'),
        ),
    ]
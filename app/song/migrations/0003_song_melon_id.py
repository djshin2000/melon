# Generated by Django 2.0.2 on 2018-02-22 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='melon_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='멜론 Song ID'),
        ),
    ]

# Generated by Django 2.0.2 on 2018-02-28 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_auto_20180228_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistyoutube',
            name='url_img_cover',
            field=models.URLField(blank=True, verbose_name='커버 이미지 URL'),
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-15 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_apikeyinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideos',
            name='search_tag',
            field=models.CharField(choices=[('hockey', 'HOCKEY'), ('football', 'FOOTBALL'), ('economy', 'ECONOMY'), ('india', 'INDIA')], max_length=200),
        ),
        migrations.AddIndex(
            model_name='youtubevideos',
            index=models.Index(fields=['published_at'], name='youtube_you_publish_6a0e3a_idx'),
        ),
    ]

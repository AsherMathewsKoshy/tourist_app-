# Generated by Django 5.1.2 on 2024-10-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='destinations/'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
    ]

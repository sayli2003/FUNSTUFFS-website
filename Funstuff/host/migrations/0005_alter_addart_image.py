# Generated by Django 4.2.3 on 2023-07-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0004_addart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
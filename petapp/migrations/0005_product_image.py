# Generated by Django 5.0 on 2024-01-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0004_product_alter_contacts2_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='images/images'),
        ),
    ]

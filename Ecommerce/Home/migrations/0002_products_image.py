# Generated by Django 4.1 on 2022-12-30 18:12

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='F:\\Riyaaz\\project\\E-commerce\\Ecommerce\\static\x07ssets\\img\\crew_neck.jpg', upload_to=Home.models.static_dir),
            preserve_default=False,
        ),
    ]
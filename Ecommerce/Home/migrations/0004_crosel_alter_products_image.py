# Generated by Django 4.1 on 2022-12-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='crosel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='F:\\Riyaaz\\project\\E-commerce\\Ecommerce\\static\\assets\\product')),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='F:\\Riyaaz\\project\\E-commerce\\Ecommerce\\static\\assets\\product'),
        ),
    ]

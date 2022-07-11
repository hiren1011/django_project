# Generated by Django 4.0.4 on 2022-07-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_product_prize_product_des_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='is_a_vendor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]

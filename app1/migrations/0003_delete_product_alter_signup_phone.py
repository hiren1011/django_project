# Generated by Django 4.0.4 on 2022-06-29 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
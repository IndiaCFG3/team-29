# Generated by Django 3.0.1 on 2020-08-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200816_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1model',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
# Generated by Django 3.0.1 on 2020-08-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200816_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1model',
            name='num_trips',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='form1model',
            name='type_waste',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 3.0.1 on 2020-08-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_form1model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1model',
            name='comments',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='form1model',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

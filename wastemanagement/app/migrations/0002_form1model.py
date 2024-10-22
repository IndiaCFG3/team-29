# Generated by Django 3.0.1 on 2020-08-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form1model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(choices=[('Choice1', 'CHOICE1'), ('Choice2', 'CHOICE2'), ('Choice3', 'CHOICE3')], max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('vehicle_number', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('num_trips', models.IntegerField()),
                ('type_waste', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('comments', models.CharField(max_length=50)),
            ],
        ),
    ]

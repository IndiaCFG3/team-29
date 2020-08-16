# Generated by Django 3.0.1 on 2020-08-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200816_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form2model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(choices=[('Choice1', 'CHOICE1'), ('Choice2', 'CHOICE2'), ('Choice3', 'CHOICE3')], max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('vehicle_number', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('num_trips', models.IntegerField(blank=True, null=True)),
                ('type_waste', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('comments', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='form1model',
            old_name='num_trips',
            new_name='input_waste',
        ),
        migrations.RenameField(
            model_name='form1model',
            old_name='quantity',
            new_name='output_waste',
        ),
        migrations.RemoveField(
            model_name='form1model',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='form1model',
            name='image',
        ),
        migrations.RemoveField(
            model_name='form1model',
            name='type_waste',
        ),
        migrations.RemoveField(
            model_name='form1model',
            name='vehicle_number',
        ),
    ]
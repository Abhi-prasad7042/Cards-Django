# Generated by Django 5.0.1 on 2024-02-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_desc', models.TextField()),
                ('car_image', models.ImageField(upload_to='carIMG')),
            ],
        ),
    ]
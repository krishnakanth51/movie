# Generated by Django 2.2.3 on 2019-08-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tktapp', '0005_remove_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(help_text='dd/mm/yyyy'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.CharField(max_length=30),
        ),
    ]

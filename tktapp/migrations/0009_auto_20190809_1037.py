# Generated by Django 2.2.3 on 2019-08-09 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tktapp', '0008_auto_20190809_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='time',
            new_name='showtime',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='price',
            new_name='ticketprice',
        ),
    ]
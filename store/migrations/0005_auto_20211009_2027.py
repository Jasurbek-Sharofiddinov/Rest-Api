# Generated by Django 3.2.8 on 2021-10-09 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20211009_1803'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_last_na_e6a359_idx',
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]
# Generated by Django 3.2 on 2022-05-04 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_orderitem_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Предмет покупки', 'verbose_name_plural': 'Предметы покупки'},
        ),
    ]
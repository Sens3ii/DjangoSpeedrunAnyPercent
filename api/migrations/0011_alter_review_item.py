# Generated by Django 3.2 on 2022-05-05 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_orderitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='api.item'),
        ),
    ]

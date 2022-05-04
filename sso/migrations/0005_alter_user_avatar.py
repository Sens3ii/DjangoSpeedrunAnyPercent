# Generated by Django 3.2 on 2022-05-04 05:45

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sso', '0004_remove_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/user/', validators=[utils.validators.validate_size, utils.validators.validate_extension]),
        ),
    ]
# Generated by Django 3.2.6 on 2022-01-25 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0002_alter_usersettings_startdate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSettings',
            new_name='UserSetting',
        ),
    ]
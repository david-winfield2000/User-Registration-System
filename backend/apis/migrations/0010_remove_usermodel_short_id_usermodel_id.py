# Generated by Django 4.1.2 on 2023-02-16 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0009_alter_usermodel_short_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='short_id',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.2 on 2023-02-16 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_alter_usermodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.CharField(default='38RqLKenTEG', max_length=11, primary_key=True, serialize=False, unique=True),
        ),
    ]
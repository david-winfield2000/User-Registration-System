# Generated by Django 4.1.2 on 2023-02-16 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_alter_usermodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.CharField(default='ffda20f8-74ac-4e49-bff1-3ded1c8636c8', editable=False, max_length=12, primary_key=True, serialize=False),
        ),
    ]

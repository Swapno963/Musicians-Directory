# Generated by Django 4.2.7 on 2023-12-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_alter_albummodel_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='release_date',
            field=models.DateField(),
        ),
    ]

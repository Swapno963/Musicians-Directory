# Generated by Django 4.2.7 on 2023-12-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_albummodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]

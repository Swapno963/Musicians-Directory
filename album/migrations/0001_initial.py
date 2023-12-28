# Generated by Django 4.2.7 on 2023-12-28 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musicialmodel')),
            ],
        ),
    ]

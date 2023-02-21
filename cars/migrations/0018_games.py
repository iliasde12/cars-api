# Generated by Django 4.1.5 on 2023-01-16 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_alter_carspersonages_linkscarssite1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameNaam', models.CharField(max_length=200, null=True)),
                ('gameAfbeelding', models.FileField(null=True, upload_to='uploads/games/afbeelding/')),
                ('gameBeschrijving', models.TextField(null=True)),
                ('CarsFilm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.carsfilms')),
            ],
        ),
    ]
# Generated by Django 4.0.1 on 2022-11-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_muziekafbeelding'),
    ]

    operations = [
        migrations.AddField(
            model_name='carspersonages',
            name='linksCarsSites',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
# Generated by Django 4.0.1 on 2022-11-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_alter_carspersonages_linkscarssite1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspersonages',
            name='linksCarsSite1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='carspersonages',
            name='linksCarsSite2',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

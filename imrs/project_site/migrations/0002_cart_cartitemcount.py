# Generated by Django 4.0.2 on 2022-04-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cartItemCount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=30)),
                ('itemCategory', models.CharField(max_length=50, null=True)),
                ('itemSubcategory', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]

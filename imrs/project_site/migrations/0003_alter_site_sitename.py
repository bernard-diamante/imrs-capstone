# Generated by Django 4.0.2 on 2022-04-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_site', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='siteName',
            field=models.CharField(max_length=50),
        ),
    ]

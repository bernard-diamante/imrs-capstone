# Generated by Django 4.0.2 on 2022-04-06 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_site', '0001_initial'),
        ('requisition', '0002_remove_materialrequisition_originsite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialrequisition',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_site.site'),
        ),
    ]

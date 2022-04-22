# Generated by Django 4.0.2 on 2022-04-04 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('transfer', models.AutoField(primary_key=True, serialize=False)),
                ('destinationSite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferDestination', to='project_site.site')),
                ('originSite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originSite', to='project_site.site')),
            ],
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-02 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('siteID', models.AutoField(primary_key=True, serialize=False)),
                ('siteName', models.CharField(max_length=50, null=True)),
                ('siteStreetNumber', models.CharField(max_length=30, null=True)),
                ('siteStreet', models.CharField(max_length=30, null=True)),
                ('siteBarangay', models.CharField(max_length=30)),
                ('siteCity', models.CharField(max_length=35)),
                ('siteProvince', models.CharField(max_length=30)),
                ('siteRegion', models.CharField(max_length=30)),
                ('siteZip', models.CharField(max_length=10)),
                ('siteContactNo', models.CharField(max_length=11)),
                ('userID', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
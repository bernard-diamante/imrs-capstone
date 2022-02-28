# Generated by Django 4.0.2 on 2022-02-21 07:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userMiddleName', models.CharField(max_length=50)),
                ('userSuffix', models.CharField(max_length=30)),
                ('userType', models.PositiveSmallIntegerField()),
                ('userContactNo', models.CharField(max_length=11)),
                ('userRole', models.PositiveSmallIntegerField(choices=[(0, 'Admin'), (1, 'Main Office'), (2, 'Warehouse Manager'), (3, 'Site Manager')], default=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=30)),
                ('itemCategory', models.CharField(choices=[('d', 'Dimensions'), ('w', 'Weight'), ('v', 'Volume'), ('a', 'Amount'), ('e', 'Equipment')], default='Dimensions', max_length=1)),
                ('itemUnitType_1', models.CharField(choices=[('d', 'Dimensions'), ('w', 'Weight'), ('v', 'Volume'), ('a', 'Amount'), ('e', 'Equipment')], default='Dimensions', max_length=1)),
                ('itemUnitType_2', models.CharField(blank=True, choices=[('mm', 'milimeter'), ('cm', 'centimeter'), ('m', 'meter'), ('mg', 'miligrams'), ('g', 'grams'), ('kg', 'kilograms'), ('in', 'inches'), ('ft', 'feet'), ('lb', 'pound'), ('t', 'tonne')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('siteID', models.AutoField(primary_key=True, serialize=False)),
                ('siteName', models.CharField(max_length=50, null=True)),
                ('siteLotNo', models.CharField(max_length=30, null=True)),
                ('siteBlockNo', models.CharField(max_length=30, null=True)),
                ('siteBarangay', models.CharField(max_length=30)),
                ('siteCity', models.CharField(max_length=35)),
                ('siteProvince', models.CharField(max_length=30)),
                ('siteRegion', models.CharField(max_length=30)),
                ('siteZip', models.CharField(max_length=10)),
                ('siteContactNo', models.CharField(max_length=11)),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Site_Item_Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteItemCount', models.PositiveIntegerField(default=0)),
                ('siteItemStatus', models.PositiveSmallIntegerField(choices=[(1, 'Normal'), (2, 'Low'), (3, 'Empty')], default=0)),
                ('itemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('siteID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.site')),
            ],
        ),
        migrations.CreateModel(
            name='Material_Requisition',
            fields=[
                ('reqID', models.AutoField(primary_key=True, serialize=False)),
                ('reqDescription', models.CharField(max_length=1000)),
                ('reqDateSubmitted', models.DateTimeField(auto_now=True)),
                ('reqDateNeeded', models.DateTimeField()),
                ('reqStatus', models.PositiveSmallIntegerField(choices=[(0, 'For Review'), (1, 'Awaiting Delivery'), (2, 'Request Denied'), (3, 'Delivered')], default=0)),
                ('originSiteID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='originSite', to='inventory.site')),
                ('reqItems', models.ManyToManyField(to='inventory.Item')),
                ('siteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinationSite', to='inventory.site')),
            ],
        ),
    ]
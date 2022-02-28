# Generated by Django 4.0.2 on 2022-02-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_user_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itemCategory',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemUnitType_1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemUnitType_2',
        ),
        migrations.AddField(
            model_name='item',
            name='itemUnitCategory',
            field=models.CharField(choices=[('d', 'Dimensions'), ('w', 'Weight'), ('v', 'Volume'), ('a', 'Amount'), ('e', 'Equipment')], default='d', max_length=1),
        ),
        migrations.AddField(
            model_name='item',
            name='itemUnitType',
            field=models.CharField(blank=True, choices=[('mm', 'milimeter'), ('cm', 'centimeter'), ('m', 'meter'), ('mg', 'miligrams'), ('g', 'grams'), ('kg', 'kilograms'), ('in', 'inches'), ('ft', 'feet'), ('lb', 'pound'), ('t', 'tonne')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='site_item_inventory',
            name='siteItemMinThreshold',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='site_item_inventory',
            name='siteItemTurnover',
            field=models.CharField(choices=[('s', 'Slow'), ('n', 'Normal'), ('f', 'Fast')], default='f', max_length=1),
        ),
        migrations.AlterField(
            model_name='site_item_inventory',
            name='siteItemStatus',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Normal'), (2, 'Low'), (3, 'Empty')], default=1),
        ),
    ]
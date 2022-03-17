# Generated by Django 4.0.2 on 2022-03-16 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0003_alter_material_requisition_reqdateneeded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material_requisition_items',
            name='quantity',
        ),
        migrations.AddField(
            model_name='material_requisition',
            name='reqItemsID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='req_items', to='requisition.material_requisition_items'),
        ),
        migrations.AddField(
            model_name='material_requisition_items',
            name='itemQuantity',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]

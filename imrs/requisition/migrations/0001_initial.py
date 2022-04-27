# Generated by Django 4.0.2 on 2022-04-27 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_site', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialRequisition',
            fields=[
                ('requisition', models.AutoField(primary_key=True, serialize=False)),
                ('reqDescription', models.TextField(blank=True, max_length=1000)),
                ('reqDateSubmitted', models.DateTimeField(auto_now=True)),
                ('reqDateNeeded', models.DateField()),
                ('reqStatus', models.PositiveSmallIntegerField(choices=[(0, 'For Review'), (1, 'Partially Filled'), (2, 'Request Denied'), (3, 'Filled'), (4, 'Delivered')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialRequisitionItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('U', 'Unfilled'), ('F', 'Filled')], default='U', max_length=1)),
                ('itemQuantity', models.PositiveIntegerField(default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
                ('requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisition.materialrequisition')),
            ],
        ),
        migrations.AddField(
            model_name='materialrequisition',
            name='reqItems',
            field=models.ManyToManyField(related_name='mat_req_items', through='requisition.MaterialRequisitionItems', to='item.Item'),
        ),
        migrations.AddField(
            model_name='materialrequisition',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_site.site'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-04-27 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_site', '0001_initial'),
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_site.site'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cartItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
        migrations.AddField(
            model_name='cart',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_site.site'),
        ),
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.UniqueConstraint(fields=('item', 'site'), name='unique_item_inv'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('cartItem', 'site')},
        ),
    ]

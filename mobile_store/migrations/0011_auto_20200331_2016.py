# Generated by Django 2.2.3 on 2020-03-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_store', '0010_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]

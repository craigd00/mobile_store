# Generated by Django 2.2.3 on 2020-04-03 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_store', '0027_review_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date',
        ),
    ]
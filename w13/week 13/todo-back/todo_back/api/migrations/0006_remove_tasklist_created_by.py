# Generated by Django 2.2 on 2019-04-21 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_tasklist_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='created_by',
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-03 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0012_testmodel_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='name',
        ),
    ]
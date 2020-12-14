# Generated by Django 3.1.2 on 2020-12-03 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizzashopapp', '0013_remove_testmodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='testuser', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
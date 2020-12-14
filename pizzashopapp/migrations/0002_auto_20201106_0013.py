# Generated by Django 3.1.2 on 2020-11-05 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizzashopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzashop',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pizzashop', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название Пиццы')),
                ('describtion', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pizza_images/')),
                ('price', models.IntegerField(default=0)),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.pizzashop')),
            ],
        ),
    ]

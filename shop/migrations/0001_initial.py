# Generated by Django 4.1.7 on 2023-12-05 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('category', models.CharField(default='Military', max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=3)),
                ('image', models.ImageField(upload_to='dron_img/')),
                ('specifications', models.TextField(max_length=500)),
                ('manufacturer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL)),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drone_order', to='shop.drone')),
            ],
        ),
    ]
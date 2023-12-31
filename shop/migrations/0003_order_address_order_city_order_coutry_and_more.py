# Generated by Django 4.1.7 on 2023-12-06 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_drone_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='coutry',
            field=models.CharField(choices=[('Poland', 'Poland'), ('Ukraine', 'Ukraine')], default='Ukraine', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_phone',
            field=models.IntegerField(null=True),
        ),
    ]

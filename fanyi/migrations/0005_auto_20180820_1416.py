# Generated by Django 2.0.1 on 2018-08-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0004_host_user_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpumonitor',
            name='gpumem_list',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='gpumonitor',
            name='gpumemused_list',
            field=models.TextField(default=''),
        ),
    ]
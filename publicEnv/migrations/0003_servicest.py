# Generated by Django 2.0.1 on 2018-11-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicEnv', '0002_auto_20181127_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sv_name', models.CharField(default='', max_length=100)),
                ('sv_host', models.CharField(default='', max_length=50)),
                ('sv_port', models.CharField(default='', max_length=10)),
                ('sv_port_type', models.IntegerField(default=0)),
                ('svninfo', models.TextField(default='')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('sv_path', models.CharField(default='', max_length=500)),
                ('host_online', models.CharField(default='', max_length=50)),
                ('path_online', models.CharField(default='', max_length=500)),
            ],
        ),
    ]

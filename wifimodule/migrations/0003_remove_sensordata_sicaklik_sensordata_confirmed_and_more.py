# Generated by Django 5.1.2 on 2024-10-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifimodule', '0002_sensordata_delete_textdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='sicaklik',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='led',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='nem',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='role',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='uzaklik',
            field=models.IntegerField(default=0),
        ),
    ]
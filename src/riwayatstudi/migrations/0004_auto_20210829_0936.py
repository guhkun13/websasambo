# Generated by Django 3.2.6 on 2021-08-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riwayatstudi', '0003_auto_20210829_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayatstudi',
            name='id_kabupaten',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='riwayatstudi',
            name='nama_kabupaten',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

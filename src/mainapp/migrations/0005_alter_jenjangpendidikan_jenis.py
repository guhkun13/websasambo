# Generated by Django 3.2.6 on 2021-08-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210828_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenjangpendidikan',
            name='jenis',
            field=models.CharField(choices=[('PMA', 'PENDIDIKAN MENENGAH ATAS'), ('PT', 'PERGURUAN TINGGI')], default='', max_length=200),
        ),
    ]

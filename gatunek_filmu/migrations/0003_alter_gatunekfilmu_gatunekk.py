# Generated by Django 4.1.3 on 2022-11-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatunek_filmu', '0002_rename_gatunek_gatunekfilmu_gatunekk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatunekfilmu',
            name='gatunekk',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, unique=True),
        ),
    ]

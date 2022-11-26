# Generated by Django 4.1.3 on 2022-11-16 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('nazwisko', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('data_zatrudnienia', models.DateField(blank=True, default=None, null=True)),
                ('wynagrodzenie', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('rola', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('data_urodzenia', models.DateField(blank=True, default=None, null=True)),
                ('econtact', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('eemail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
            ],
            options={
                'db_table': 'pracownik',
            },
        ),
    ]

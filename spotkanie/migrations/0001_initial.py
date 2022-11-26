# Generated by Django 4.1.3 on 2022-11-25 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film', '0004_alter_film_nazwa'),
        ('studio', '0002_alter_studio_nazwa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spotkanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('data_rozpoczecia', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('godzina', models.TimeField(auto_now=True)),
                ('id_film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_filmu', to='film.film', to_field='nazwa')),
                ('id_lokalizacja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_studia', to='studio.studio', to_field='nazwa')),
            ],
            options={
                'db_table': 'spotkanie',
            },
        ),
    ]
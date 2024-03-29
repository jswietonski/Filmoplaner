# Generated by Django 4.1.3 on 2022-11-25 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film', '0004_alter_film_nazwa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kosztorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koszt_produkcji', models.IntegerField(blank=True, default=None, null=True)),
                ('koszt_postprodukcji', models.IntegerField(blank=True, default=None, null=True)),
                ('koszt_marketingu', models.IntegerField(blank=True, default=None, null=True)),
                ('koszt_calkowity', models.IntegerField(blank=True, default=None, null=True)),
                ('id_filmm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_filmuu', to='film.film', to_field='nazwa')),
            ],
            options={
                'db_table': 'kosztorys',
            },
        ),
    ]

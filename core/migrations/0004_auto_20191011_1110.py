# Generated by Django 2.2.6 on 2019-10-11 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191009_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamowienie',
            name='data_urodzenia',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='data_uslugi',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='data_śmierci',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='imie_zmarłego',
            field=models.CharField(default='kejbi', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='kwatera',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='nazwisko_zmarłego',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='nr_grobu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='rząd',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
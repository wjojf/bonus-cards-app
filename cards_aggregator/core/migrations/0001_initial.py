# Generated by Django 4.1.3 on 2022-11-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField(default=0, verbose_name='Card series')),
                ('number', models.PositiveIntegerField(default=8888, verbose_name='Номер карты')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_expired', models.DateTimeField(null=True)),
                ('last_used', models.DateTimeField(auto_now=True)),
                ('balance', models.FloatField(default=0.0, verbose_name='Баланс карты')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active'), ('Expired', 'Expired')], max_length=150)),
            ],
            options={
                'ordering': ('-date_created', '-last_used'),
                'unique_together': {('series', 'number')},
            },
        ),
    ]

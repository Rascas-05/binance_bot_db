# Generated by Django 5.1.3 on 2024-11-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='BTCUSDT', max_length=8)),
                ('open_time', models.DateTimeField()),
                ('close_time', models.DateTimeField()),
                ('open', models.DecimalField(decimal_places=8, max_digits=24)),
                ('high', models.DecimalField(decimal_places=8, max_digits=24)),
                ('low', models.DecimalField(decimal_places=8, max_digits=24)),
                ('close', models.DecimalField(decimal_places=8, max_digits=24)),
                ('volume', models.IntegerField()),
                ('quote_volume', models.IntegerField()),
                ('number_trades', models.IntegerField()),
                ('taker_buy_base_volume', models.IntegerField()),
                ('taker_buy_quote_volume', models.IntegerField()),
            ],
        ),
    ]
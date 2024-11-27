from django.db import models

class Klines(models.Model):
    code = models.CharField(max_length=8, default="BTCUSDT")
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    open = models.DecimalField(decimal_places=8, max_digits=24)
    high = models.DecimalField(decimal_places=8, max_digits=24)
    low = models.DecimalField(decimal_places=8, max_digits=24)
    close = models.DecimalField(decimal_places=8, max_digits=24)
    volume = models.FloatField()
    quote_asset_volume = models.FloatField()
    number_of_trades = models.FloatField()
    taker_buy_base_asset_volume = models.FloatField()
    taker_buy_quote_asset_volume = models.FloatField()
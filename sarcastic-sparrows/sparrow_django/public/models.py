from django.db import models
from django_matplotlib import MatplotlibFigureField


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    ticker_symbol = models.CharField(max_length=5)
    open = models.DecimalField(max_digits=20, decimal_places=5)
    high = models.DecimalField(max_digits=20, decimal_places=5)
    low = models.DecimalField(max_digits=20, decimal_places=5)
    close = models.DecimalField(max_digits=20, decimal_places=5)
    volume = models.IntegerField()
    fig = MatplotlibFigureField(figure="my_figure")

    def __str__(self):
        return "Name: <%r> Date: <%r> High: <%.4f> Low: <%.4f>" % (
            self.ticker_symbol,
            str(self.date),
            self.high,
            self.low,
        )


# class Portfolio(models.Model):
#

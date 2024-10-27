from django.db import models

class Weigh(models.Model):
    weigh = models.DecimalField(max_digits = 10, decimal_places = 3)
    created_on = models.DateTimeField(auto_now_add = True)



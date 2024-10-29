from django.db import models

class Weigh(models.Model):
    value = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_on = models.DateField(auto_now_add = True)

    def __str__(self): 
        return f"{self.value} {self.created_on}"


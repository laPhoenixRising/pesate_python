from django.db import models

class Weigh(models.Model):
    value = models.DecimalField(max_digits = 10, decimal_places = 3)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self): 
        return f"{self.value} {self.created_on}"


from django.db import models

class CustomerDetails(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    customer_id = models.IntegerField()
    order_id = models.IntegerField()



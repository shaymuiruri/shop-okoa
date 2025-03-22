from django.db import models

# Create your models here.
#Shopokoa data base model
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    tag_id = models.CharField(max_length=30, unique=True)
    amount_saved = models.DecimalField(max_digits=10, decimal_places=2)
    credit_available = models.DecimalField(max_digits=10, decimal_places=2)
    trust_score_token = models.CharField(max_length=10)
    USER_TYPE_CHOICES = (
        ('provider', 'Provider'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

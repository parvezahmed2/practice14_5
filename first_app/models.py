from django.db import models

# Create your models here.

class PracticeModel(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.IntegerField(primary_key=True)
    email_field = models.EmailField()
    big_integer_field = models.BigIntegerField()
    binaryField = models.BinaryField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    image_field = models.ImageField(upload_to='images/')
    generic_ip_address_field = models.GenericIPAddressField()
    json_field = models.JSONField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()
    time_field = models.TimeField()
    small_integer_field = models.SmallIntegerField()
    slug_field = models.SlugField()






from django.db import models

# Create your models here.
class Branch(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        managed = False
        db_table = 'branches'
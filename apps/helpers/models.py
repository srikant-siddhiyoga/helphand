from django.db import models
import uuid

#---------------------------------------------------------------
# Helpers model
#---------------------------------------------------------------
class Helpers(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=255)
    helper_type = models.ForeignKey('HelperTypes', on_delete=models.CASCADE)
    cost = models.FloatField()
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=6)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

#---------------------------------------------------------------
# Helper types model
#---------------------------------------------------------------
class HelperTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
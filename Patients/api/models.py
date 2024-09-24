from django.db import models
import datetime

# Create your models here.
class Patient(models.Model):  
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)  
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    
    def get_age(self):
        age = datetime.date.today() - self.date_of_birth
        return int(age.days / 365.25)
    
    def get_address(self):
        address = f"{self.street}, {self.city}, {self.state}, {self.zip_code}, {self.country}"
        return address
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
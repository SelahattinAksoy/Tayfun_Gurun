from django.db import models

# Create your models here.


class Order(models.Model):
        id = models.AutoField(primary_key=True)
        first_name = models.CharField(max_length=30,verbose_name="Ad")
        last_name = models.CharField(max_length=30,verbose_name="Soyad")
        mail = models.CharField(max_length=30,verbose_name="Mail")
        date = models.DateField()
        phone_number = models.CharField(max_length=12,verbose_name="Tel")
        message = models.TextField(verbose_name="Mesaj") 
      
        def __str__(self):
            return self.first_name
    

class Service(models.Model):
        id = models.AutoField(primary_key=True)
        hizmet = models.CharField(max_length=30,verbose_name="Hizmet")
        price = models.CharField(max_length=30,verbose_name="Fiyat") 

        def __str__(self):
          return self.hizmet

class Customer(models.Model):
         phone_number = models.CharField(primary_key=True,max_length=12,verbose_name="Tel")
         mail = models.CharField(max_length=30,verbose_name="Mail")
         first_name = models.CharField(max_length=30,verbose_name="Ad")
         last_name = models.CharField(max_length=30,verbose_name="Soyad")
         
         
         def __str__(self):
           return self.mail
from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import math, datetime
from django.conf import settings
from django.db.models import Count, Avg
from django.core.files.images import ImageFile
from datetime import date



STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)

APP_CHOICES = (
    ('PS', 'PhotoShop'), ('LR', 'LightRoom')
)

USER_CHOICES = (
    ('Admin', 'Admin'), ('User', 'User')
)



class Photographers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
   
    picture = StdImageField(null=True, blank=True,  variations={
       'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })
   
    phone = models.CharField(max_length=20, blank=False)
    cpf = models.CharField(max_length=19, null=True, blank=True)
    cnpj = models.CharField(max_length=19, null=True, blank=True)
    birthday = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    district = models.CharField(max_length=30, null=True, blank=True)
    zip_code = models.CharField(max_length=25, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, null=True, blank=True)
    type_user = models.CharField(max_length=50, choices=USER_CHOICES, blank=False)
    password1 = models.CharField(max_length=15, blank=False)
    
    
    
    def __unicode__(self):
    	    return self.name

    @receiver(post_save, sender=User)
    def new_register(sender, instance, created, **kwargs):
        if created:
            Photographers.objects.create(user=instance)
        instance.photographers.save()

    
    def __str__(self):
        return str(self.name)  + ' - ' + str(self.lastname)


class Images(models.Model):
    name = models.ForeignKey(Photographers, on_delete=models.CASCADE, blank=False)
    client = models.CharField(max_length=50, blank=False)
    number = models.IntegerField( blank=False)
    pictures = models.IntegerField( blank=False)
    checkin = models.DateField (max_length=50, blank=False)
    checkout = models.DateField(max_length=50, null=True, blank=True)
    deadline = models.DateField(max_length=50, null=True, blank=True)
    app = models.CharField(max_length=50, choices=APP_CHOICES, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    link = models.CharField(max_length=50, null=True, blank=True)
    info = models.TextField(max_length=255, blank=False)

    def __str__(self):
        return str(self.name)  + ' - ' + str(self.checkin) + ' - ' + str(self.pictures)

    

class Payment(models.Model):
    name = models.ForeignKey(Photographers, on_delete=models.CASCADE, blank=False)
    value = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    checkin = models.DateField (max_length=50, blank=False)
    
    def __str__(self):
        return str(self.name)  + ' - ' + str(self.value) + ' - ' + str(self.checkin)

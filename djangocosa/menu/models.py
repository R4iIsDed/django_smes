from django.db import models

# Create your models here.

class Tabla1(models):
    codigoTabla1= models.AutoField(primary_key=True)
    nombre = models.AutoField(max_length=20)
    
class tabla2(models):
    codigoTabla2= models.AutoField(primary_key=True)
    nombre2 = models.AutoField(max_length=30,null= True,blank=False)
    edad = models.IntegerField()
    Foto = models.ImageField(upload_to="tabla2_images")
    tabla1 = models.ForeignKey(Tabla1,on_delete=models.CASCADE)
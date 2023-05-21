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

class region(models):
    id_reg=models.AutoField(primary_key=True)
    nombre=models.AutoField(max_length=20)

class comuna(models):
    id_com=models.AutoField(primary_key=True)
    nombre=models.AutoField(max_length=20)
    fk_id_reg=models.ForeignKey(region,on_delete=models.CASCADE)

class rol(models):
    id_rol=models.AutoField(primary_key=True)
    nombre=models.AutoField(max_length=30)

class preguntas(models):
    id_preg=models.AutoField(primary_key=True)
    nombre=models.AutoField(max_length=30)

class usuario(models):
    id_usuario=models.AutoField(primary_key=True)
    rut=models.AutoField(max_length=)
    nombres=models.AutoField(max_length=)
    apellidos=models.AutoField(max_length=)
    telefono=models.AutoField(max_length=)
    correo=models.AutoField(max_length=)
    clave=models.AutoField(max_length=)
    fk_rol=models.ForeignKey(rol,on_delete=models.CASCADE)
    fk_preg=models.ForeignKey(preguntas,on_delete=models.CASCADE)
    respuesta=models.AutoField(max_length=)

class direccion(models):
    id_direc=models.AutoField(primary_key=True)
    calle=models.AutoField(max_length=30)
    num=models.AutoField(max_length=20)
    codigo_po=models.AutoField(max_length=30)
    fk_comuna=models.ForeignKey(comuna,on_delete=models.CASCADE)
    fk_usuario=models.ForeignKey(usuario,on_delete=models.CASCADE)
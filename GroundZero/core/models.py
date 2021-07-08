from django.db import models

# Create your models here.
class Tipomoneda(models.Model):
    idmoneda = models.IntegerField(primary_key=True, verbose_name='id tipo moneda')    
    monedapago=models.CharField(max_length=20, verbose_name='moneda (peso o dolar)')
    

    def __str__(self) :
        return self.monedapago


class Proveedor(models.Model):
    idproveedor = models.IntegerField(primary_key=True, verbose_name='numero de identificacion')
    fotografia=models.ImageField()
    nombreproveedor=models.CharField(max_length=50, verbose_name='nombre proveedor')
    telefonoproveedor=models.IntegerField(verbose_name='telefono proveedor')
    direccionproveedor=models.CharField(max_length=50, verbose_name='direccion proveedor')
    emailproveedor=models.EmailField(max_length=40, verbose_name='email proveedor')
    paisproveedor=models.CharField(max_length=30, verbose_name='pais proveedor')
    passproveedor=models.CharField(max_length=15, verbose_name='pass proveedor')
    moneda=models.ForeignKey(Tipomoneda, on_delete=models.CASCADE)

    def __str__(self) : 
        return self.nombreproveedor


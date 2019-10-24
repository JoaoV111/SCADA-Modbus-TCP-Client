from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=200)
    client_img = models.ImageField(upload_to = 'client_img/', null=True)

    def __str__(self):
        return self.name


class CLP(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    ip_int = models.CharField(max_length=200)
    ip_ext = models.CharField(max_length=200)
    port = models.IntegerField(default=0)
    clp_img = models.ImageField(upload_to = 'clp_img/', null=True, blank=True)

    def __str__(self):
        return self.name


class Equipamento(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    clp = models.ForeignKey(CLP, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    end_modbus_leitura = models.IntegerField(default=0)
    end_modbus_escrita = models.IntegerField(default=0)
    status = models.CharField(max_length=200, null=True, blank=True)
    equip_img = models.ImageField(upload_to = 'equip_img/', null=True, blank=True)

    def __str__(self):
        return self.name


class Value(models.Model):
    clp = models.ForeignKey(CLP, on_delete=models.CASCADE)
    end = models.IntegerField(default=0)
    value = models.IntegerField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return (self.clp.name + '/ end: ' + str(self.end) + '/ value: '
                + str(self.value) + '/ Date: ' + str(self.date))


class Task(models.Model):

    class Meta:
        permissions = [
            ("escritorio", "Tela Escritório"),
            ("cnb", "Tela CNB"),
                    ]
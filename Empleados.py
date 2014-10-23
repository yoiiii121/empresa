#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'

class Empleado():
    def __init__(self,nombre,apellidos,dni,direccion, edad, email, salario):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__dni=dni
        self.__direccion=direccion
        self.__edad=edad
        self.__email=email
        self.__salario=salario

    def get_salario(self):
        return round(self.__salario,2)
    def get_dni(self):
        return self.__dni
    def get_nombre_completo(self):
        return (self.__nombre+' '+self.__apellidos)
    def get_edad(self):
        return int(self.get_edad())
    def get_email(self):
        return str(self.get_email())
    def get_direccion(self):
        return str(self.get_direccion())
    def get_salario_menusal(self):
        return float(round(self.get_salario()/12.0,2))
    def __str__(self):
        return 'Nombre ' + self.get_nombre_completo()+ ' Dni ' + self.get_dni() + ' Salario ' + str(self.get_salario()) + ' Salario mensual '+ str(self.get_salario_menusal())
    property(get_dni)
    property(get_edad)
    property(get_email)
    property(get_direccion)
    property(get_nombre_completo)
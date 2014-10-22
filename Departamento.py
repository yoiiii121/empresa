#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'

from Empleados import Empleado
class Departamento():
    def __init__(self,nombre_depto,id_depto):
        self.__nombre_depto=nombre_depto
        self.__id_depto=id_depto
        self.__empleado=[]
    def anyadir_emplado(self,empleado):
        self.__empleado.append(empleado)
    def get_salario_total(self):
        return float(sum([i.get_salario() for i in self.__empleado]))
    def __str__(self):
        return 'Salario total ' + str(self.get_salario_total())
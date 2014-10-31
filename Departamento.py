#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'


class Departamento():
    def __init__(self, nombre_depto, id_depto):
        self.__nombre_depto = nombre_depto
        self.__id_depto = id_depto
        self.__empleado = []

    def anyadir_emplado(self, empleado):
        self.__empleado.append(empleado)

    def get_salario_total(self):
        return round(float(sum([i.get_salario() for i in self.__empleado])), 2)

    def get_salario_total_mensual(self):
        return round(float(sum([i.get_salario_menusal() for i in self.__empleado])), 2)

    def get_nombre_depto(self):
        return self.__nombre_depto

    def __str__(self):
        return 'Salario total ' + str(self.get_salario_total()) + 'Salario total mensual' + str(
            self.get_salario_total_mensual())
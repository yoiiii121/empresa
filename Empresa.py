#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'


class Empresa():
    def __init__(self, nombre_empresa, cif, razon_social):
        self.__nombre_empresa = nombre_empresa
        self.__cif = cif
        self.__razon_social = razon_social
        self.__departamentos = []
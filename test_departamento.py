#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from Empleados import Empleado
from Departamento import Departamento
__author__ = 'Nacho-w7'

from mockito import *

class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        em1= mock(Empleado)
        when(em1).get_salario().thenReturn(1000.56)
        em2= mock(Empleado)
        when(em2).get_salario().thenReturn(954.23)
        em3= mock(Empleado)
        when(em3).get_salario().thenReturn(1000.56)
        dep1= Departamento('Movistar','id001')
        self.assertIsInstance(dep1.get_salario_total(),float)
        self.assertEqual(dep1.get_salario_total(),0.0)
        dep1.anyadir_emplado(em1)
        self.assertEqual(dep1.get_salario_total(),1000.56)
        dep1.anyadir_emplado(em2)
        self.assertEqual(dep1.get_salario_total(),1954.79)
        dep1.anyadir_emplado(em3)
        self.assertEqual(dep1.get_salario_total(),2955.35)

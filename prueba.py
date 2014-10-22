#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'
from Departamento import Departamento
from Empleados import Empleado

print 'Creo 3 empleados\n'
em1= Empleado('Ada','Gomez','22222222B','Kansas city',35,'pp@pp.pp',1000.56)
em2= Empleado('Ana','Sanchez','33333333C','Eduardo dato',45,'ll@ll.ll',954.23)
em3= Empleado('Angela','Muñiz','44444444D','Melendez Pelayo',23,'ee@ee.ee',1000.56)

print em1
print em2
print em3

print 'Creo un departamento\n'
dep1= Departamento('Movistar','id001')


print 'añado 3 empleados\n'
dep1.anyadir_emplado(em1)
dep1.anyadir_emplado(em2)
dep1.anyadir_emplado(em3)


print dep1
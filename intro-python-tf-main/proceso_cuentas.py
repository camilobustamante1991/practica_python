#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Ana
import csv
from persona import Persona


def crear_cuentas():
    """
    param: None
    :return: Lista de diccionarios
    """
    personas = {}
    archivo = open("personas.csv", "r")
    archivo_csv = csv.reader(archivo)
    titulos = next(archivo_csv)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        persona = Persona(dni, nombre, fecha_nacimiento)
        persona.crear_cuenta()
        # La parte mas importante donde agrego al diccionario
        # con clave = dni el objecto persona
        personas[dni] = persona
    archivo.close()
    return personas


def procesar_gastos(cuentas, archivo):
    with open(archivo) as f:
    reader = csv.reader(f)
    titles = next(reader)
    for acount in cuentas:
        for line in reader:
            if acount.dni == line[1]:
                total_moviemientos=0
                descripcion_movimiento = "gasto"
                for movimiento in acount.movimientos:
                    if descripcion_movimiento in movimiento.descripcion:
                        total_moviemientos = total_moviemientos + movimiento.monto                    
                acount.cantidad = acount.cantidad - total_moviemientos
    return acounts


def procesar_depositos(cuentas, archivo):
    with open(archivo) as f:
    reader = csv.reader(f)
    titles = next(reader)
    for acount in cuentas:
        for line in reader:
            if acount.dni == line[1]:
                total_moviemientos=0
                descripcion_movimiento = "deposito"
                for movimiento in acount.movimientos:
                    if descripcion_movimiento in movimiento.descripcion:
                        total_moviemientos = total_moviemientos + movimiento.monto                    
                acount.cantidad = acount.cantidad + total_moviemientos
    return acounts


def procesar_transferencias(cuentas, archivo):
    with open(archivo) as f:
    reader = csv.reader(f)
    titles = next(reader)
    for acount in cuentas:
        for line in reader:
            if acount.dni == line[1]:
                total_moviemientos=0
                descripcion_movimiento = "deposito"
                for movimiento in acount.movimientos:
                    if descripcion_movimiento in movimiento.descripcion:
                        total_moviemientos = total_moviemientos + movimiento.monto                    
                acount.cantidad = acount.cantidad + total_moviemientos
    return acounts

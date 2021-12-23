#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Ana
import datetime


class Cuenta(object):

    def __init__(self, monto_inicio=0, numero_de_cuenta=0):  # contructor, siempre de la misma forma
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True

    def aplicar_gasto(self, monto):  # retirar
        if self.activa == True
            self.cantidad = self.cantidad - monto
            self.crear_movimiento("Estamos aplicando un gasto", monto)

    def aplicar_deposito(self, monto):  # ingresar       
        if self.activa == True
            self.cantidad = self.cantidad + monto
            self.crear_movimiento("Estamos aplicando un deposito", monto)

    def desactivar(self):
        if self.cantidad == 0 :
            self.activa = False

    def activar(self):
        if self.cantidad == 0 :
            self.activa = True

    def crear_movimiento(self, descripcion, monto):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)

    def __str__(self):       
        print(f"CUENTA comun {self.cantidad} con numero {self.numero_de_cuenta}")


class CuentaJoven(Cuenta):

    def __init__(self, bonificacion, monto_inicio=0, numero_de_cuenta=0):
        Cuenta.__init__(self, monto_inicio, numero_de_cuenta)
        self.bonificacion = bonificacion

    def __str__(self):
        # TODO: Completar para que quede mejor
        print(f"CUENTA JOVEN {self.cantidad} con numero {self.numero_de_cuenta}")


class MovimientoCuenta(object):

    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        # TODO: Completar como pide el ejercicio 3)
        return f"{self.fecha_y_hora} {self.descripcion} {self.monto}"

# Josue Guadalupé Palacios Franco-25
from abc import ABC, abstractmethod
import os
os.system("cls")
class Empleado_j25(ABC):
    def __init__(self, apellidos, rfc, nombre):
        self.__apellidos = apellidos
        self.__rfc = rfc
        self.__nombre = nombre

class EmpleadoVendedor(Empleado_j25):
    def __init__(self, apellidos, rfc, nombre, monto_vendido, tasa_comision):
        super().__init__(apellidos, rfc, nombre)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision
    def calcular_ingresos(self):
        return (self.monto_vendido * self.tasa_comision)
    def calcular_bonificacion(self):
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return ((self.calcular_ingresos()) * 0.05)
        elif self.monto_vendido>5000:
            return ((self.calcular_ingresos()) * 0.10)
    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return ingresos * 0.11
        else:
            return ingresos * 0.15
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        sueldo_neto = ingresos + bonificacion - descuento
        if sueldo_neto < 150:
            raise ValueError("El salario neto no puede ser menor al salario mínimo a 150 pesos")#Excepcion
        return sueldo_neto
    def mostrar_info(self):
        return {"RFC": self._Empleado_j25__rfc,"Apellidos": self._Empleado_j25__apellidos,"Nombre": self._Empleado_j25__nombre,
            "Monto vendido": self.monto_vendido,"Tasa comisión": self.tasa_comision,"Sueldo Neto": self.calcular_sueldo_neto()}
           
class EmpleadoPermanente(Empleado_j25):
    def __init__(self, apellidos, rfc, nombre, sueldo_base, num_seguro_social):
        super().__init__(apellidos, rfc, nombre)
        self.sueldo_base = sueldo_base
        self.num_seguro_social = num_seguro_social
    def calcular_ingresos(self):
        return self.sueldo_base
    def calcular_descuento(self):
        return self.sueldo_base * 0.11
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        descuento = self.calcular_descuento()
        sueldo_neto = ingresos - descuento
        if sueldo_neto < 150:
            raise ValueError("El salario neto no puede ser menor al salario mínimo de 150 pesos")
        return sueldo_neto
    def mostrar_info(self):
        return {"RFC": self._Empleado_j25__rfc,"Apellidos": self._Empleado_j25__apellidos,"Nombre": self._Empleado_j25__nombre,"Sueldo Base": self.sueldo_base,
                "Número de Seguro Social": self.num_seguro_social,"Sueldo Neto": self.calcular_sueldo_neto()}

empleado_vendedor = EmpleadoVendedor("exe", "ABC123", "sonic", 3000, 0.1)
print(empleado_vendedor.mostrar_info())
print("*"*150)
empleado_permanente = EmpleadoPermanente("ozuna", "XYZ456", "Sech", 5000, "123456789")
print(empleado_permanente.mostrar_info())

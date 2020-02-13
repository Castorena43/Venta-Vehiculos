from Vehiculo import Vehiculo


class Empleado():
    def __init__(self, nombre, salario = 500):
        self.__nombre = nombre
        self.__salario = salario 
        self.__vVendidos = []
        self.__comisiones = 0
        self.__bono = 0

    def set_vVendidos(self,lista):
        for list in lista:
            self.__vVendidos.append(list)
            self.__comisiones += list['comision']
            self.__bono += 1000

    def getNombre(self):
        return self.__nombre

    def getSalario(self):
        return self.__salario
    
    def getComisiones(self):
        return self.__comisiones

    def getBono(self):
        return self.__bono
    
    def getvVendidos(self):
        return self.__vVendidos
    
    def addVehiculo(self, vehiculo):
        self.__comisiones += vehiculo.getComision()
        self.__bono += 1000
        self.__vVendidos.append(vehiculo)

    def addVehiculoMongo(self, vehiculo):
        self.__comisiones += vehiculo.getComision()
        self.__bono += 1000
        self.__vVendidos.append({
            "marca":vehiculo.getMarca(),
            "modelo":vehiculo.getModelo(),
            "precio":vehiculo.getPrecio(),
            "comision":vehiculo.getComision()
        })

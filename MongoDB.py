from pymongo import MongoClient
from Vehiculo import Vehiculo
from Empleado import Empleado


class Mongo():
    def __init__(self):
        self.__MONGO_URI = 'mongodb://localhost'
        self.__client = MongoClient(self.__MONGO_URI)
        self.__db = self.__client['ventas_autos']
        self.__cEmpleados = self.__db['empleados']

    def insertarEmpleado(self, empleado):
        self.__cEmpleados.insert_one({
            "_id" : self.__cEmpleados.find().count()+1,
            "nombre" : empleado.getNombre(),
            "salario" : empleado.getSalario(),
            "vVendidos" : [],
            "bono" : empleado.getBono(),
            "comisiones" : empleado.getComisiones()
        })
    
    def insertarAuto(self, auto, bono, comisiones):
        empleado = self.__cEmpleados.find_one({"_id" : self.__cEmpleados.find().count()})
        lista = empleado['vVendidos']
        lista.append({
            "marca" : auto.getMarca(),
            "modelo" : auto.getModelo(),
            "precio" : auto.getPrecio(),
            "comision" : auto.getComision()
        })
        self.__cEmpleados.update_one({"_id" : self.__cEmpleados.find().count()},{"$set" : {"vVendidos" : lista, "bono" : bono, "comisiones" : comisiones}})

    def cerrarConexion(self):
        self.__client.close()

    def consultarEmpleados(self):
        empleados = self.__cEmpleados.find()
        c = 0
        c = empleados.count()
        for e in empleados:
            print(str(e['_id'])+'.- '+e['nombre'])
        return c

    def editar(self,id):
        consulta = self.__cEmpleados.find_one({"_id":id})
        empleado = Empleado(consulta['nombre'])
        empleado.set_vVendidos(consulta['vVendidos'])
        respuesta = input('¿Agregar un automóvil? (s/n): ')
        while not respuesta == 'n':
            marca = input('Ingresa la marca: ')
            modelo = input('Ingresa el modelo: ')
            precio = float(input('Ingresa el precio: '))
            v = Vehiculo(marca, modelo, precio)
            empleado.addVehiculoMongo(v)
            respuesta = input('¿Agregar un automóvil? (s/n): ')
        self.__cEmpleados.update_one({"_id":id},
                {
                    "$set":
                        {
                            "salario": empleado.getSalario(),
                            "bono":empleado.getBono(),
                            "comisiones":empleado.getComisiones(),
                            "vVendidos":empleado.getvVendidos()
                        }
                }
        )


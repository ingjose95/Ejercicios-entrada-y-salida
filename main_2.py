# Primer acceso: creación de un nuevo archivo txt para almacenar datos de una clase


# f = open('vehiculo.txt', 'w')


# segundo acceso: vaciado de datos a archivo txt


class Vehiculo:

    marca = ' '
    modelo = ' '


    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    def descripcion(self):

        return f'La marca del vehiculo es {self.marca} y el modelo es {self.modelo}.'

v = Vehiculo('Toyota', 'B4-700')

# Luego, se procede a abrie el archivo txt previamente creado. Se añadirá el objeto creado.

f = open('vehiculo.txt', 'w')

f.write(v.descripcion())

f.close()

#Primer acceso: se crea el archivo txt donde se almacenarán los datos

# f = open('animales.txt', 'w')

# segundo acceso: escritura de datos en archi txt existente

f = open('animales.txt', 'w')

nombre_animales = 'Perro \nGato \nVaca'

lista_animales = f.write(nombre_animales)

f.close()
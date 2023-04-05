#1. Importar cosas
import os
from pathlib import Path
"""
print("Holi con os")
print(os.getcwd()) #Devuelve la ruta de trabajo

from pathlib import Path  #Lo mismo, pero más barato
print("Holi desde Path")
print(Path.cwd())

print(type(os.getcwd()))
print(type(Path.cwd()))
"""
#Obtener los archivos en una ruta
#print(os.listdir()) #Obtenemos una lista con los elementos de la carpeta
#print(os.listdir('Example4')) #Accedemos a los archivos de una carpeta específica

#Crear carpetas usando python
"""
os.mkdir('Example5') #Creamos carpetas
Path('Example6').mkdir() #Creamos carpetas de otra forma
Path('Example6').mkdir(exist_ok=True) #Evitamos que se creen carpetas repetidas
"""
#Crear carpetas dentro de carpetas
#os.makedirs(os.path.join('Example7','Example8'))

#Renombrar archivos
#os.rename('Example7', 'Example10')

for file in os.listdir():
    if file.endswith('.csv'):
        os.rename(file,f'2023_tarea_{file}')

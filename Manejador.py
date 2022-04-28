from ClasesPlan import ClasesPlan
import csv

class ManejadorPlanes:
    __lista=[]
    
    def __init__(self):
        self.iniciar()
        
    def iniciar(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            UnRegistro=ClasesPlan(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.__lista.append(UnRegistro)
            
    def actualizar(self):
        for i in range(self.__lista):
            print('Codigo Plan: {} '.format(self.__lista[i].getcodPlan()))
            print('Modelo: {}'.format(self.__lista[i].getmodelo()))
            print('Version:{} '.format(self.__lista[i].getversion()))
            nuevo=input('Ingrse valor nuevo del vehiculo:')
            self.__lista[i].nuevovalor(nuevo)
            
            
            

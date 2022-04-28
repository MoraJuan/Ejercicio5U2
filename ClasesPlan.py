class ClasesPlan:
    __codplan= ''
    __modelo= '' 
    __version=''
    __valorvehiculo = ''
    __cantcuota=''
    __cantlicveh=''

def __init__(self,codplan,modelo,version, valorvehiculo,cantcuota, cantlicveh):
    self.__codplan= codplan
    self.__modelo = modelo
    self.__version = version
    self.__valorvehiculo= valorvehiculo
    self.__cantcuota= cantcuota
    self.__cantlicveh= cantlicveh
    
def getcodPlan(self):
    return self.__codplan
def getmodelo(self):
    return self.__modelo
def getversion(self):
    return self.__version
def getvalorVehiculo(self):
    return self.__valorVehiculo
def getcantCuota(self):
    return self.__cantCuota
def getcantLicVeh(self):
    return self.__cantLicVeh
def nuevovalor(self, nuevo):
    self.__valorVehiculo=nuevo
    return self.__valorVehiculo
    

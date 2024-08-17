"""entrada = "abcd"
salida = ""

for i in entrada:
    salida += i * 3
print(salida)"""

# Herencia y Poliformismo

"""class Vehiculo: 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"{self.marca} {self.modelo} está acelerando"

class Carro(Vehiculo):
    def acelerar(self):
        return f"{self.marca} {self.modelo} está acelerando"

class Motocicleta(Vehiculo):
    def caballito(self):
        return f"{self.marca} {self.modelo} está haciendo un caballito"


carro = Carro ("Toyota", "TXL")
moto = Motocicleta("Ducati", "1199")

#Heredar datos
print(carro.acelerar())
print(moto.caballito())

#-----------------------------------------------------------------------------

#Poliformismo
print(carro.arrancar())"""

# MANEJO DE ERRORES

numero1 = 5
numero2= 1
numero1 = "1"

try:
    #INTENTA EJECUTAR
    print(numero1 + numero2)

except:
    #SE EJECUTA SI HAY UN PROBLEMA
    print("Se ha producido un error")

print("_____________________________________________")

#FLUJO COMPLETO DE UNA EXPRESION
try:
    #INTENTA EJECUTAR
    print(numero1 + numero2)
    print("No procede ningun error")

except:
    #SE EJECUTA SI HAY UNA EXCEPCION
    print("Se ha producido un error")

else: 
    #OPCIONAL SI SE EJECUTA Y NO PROCEDE NINGUNA EXCEPCION
    print("No se presenta ningun error, se sigue ejecutando de manera normal")

finally:
    #OPCIONAL SIEMPRE SE EJECUTA HAYAN O NO HAYAN EXCEPCIONES
    print("La ejecucion continuacion")

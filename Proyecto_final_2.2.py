global lista
lista = [] #es lo mismo que declarar lista= list()
#aqui voy a guardar los resultados de cada movimiento
white open("Transacciones.txt") as archivo
archivo = open (nombreArchivo,"a")
archivo.close()

#whit open("fichero.txt","r") as f

from datetime import date
import requests
import json

class Transacciones:
    nroT = 0 #numero de transacción
    codID = 0 #codigo de usuario
    sym = "" #symbolo de criptomoneda
    nom = "" #nombre de criptomoneda
    cantCM = 0.00 #cantidad de criptomoneda
    fecha =date.today() #fecha de la transacción
    tipo ="" #tipo de transacción
    usd = 0  #conversión de la criptomoneda a USD a cotización del día

_ENDPOINT = "https://api.binance.com"
def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos:
        return True
    else:
        return False

def esnumero(numero): #determina si el valor ingresado es un numero
    return numero.replace('.','',1).isdigit()

def codigoID(codigo): #usuario valido diferente del propio
    if codigo == usuario:
        return False
    else:
        return True

def  recibirCripto(): #opcion 1
    trans = Transacciones()      
    monedas_dict = {"BTC":"Bitcoin","BCC":"BitConnect","LTC":"Litecoin","ETH":"Ethereum","ETC":"Ethereum Classic","XRP":"XRP"}
    user =input(">Ingrese el codigo del destinatario.")
    while not codigoID(user):
        user = input(">Ingrese el codigo del destinatario.\n (debe ser diferente al propio): ")
    else:
        print("Usuario Valido")    
    moneda = input(">Ingrese el simbolo de la moneda deseada:\n (BTC,BCC,LTC,ETH,ETC,XRP): " )
    while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda= input(">Ingrese el simbolo de la moneda deseada:\n (BTC,BCC,LTC,ETH,ETC,XRP): ")
    else:
        print("Moneda Valida")
        cant= ""
        while not esnumero(cant):
            cant = input(">Ingrese la cantidad a recibir de la criptomoneda: ")   
    trans.codID = user 
    trans.sym = moneda
    trans.nom = monedas_dict.get(moneda)
    trans.cantCM = float(cant)    
    trans.fecha =date.today()
    trans.tipo = "Transferencia Recibida"
    trans.nroT= 0
    lista.append(trans)
    
    archivo = open(nombreArchivo,"a")
    json.dump(lista,archivo)
    archivo.close()
        


def transferirMonto(): #opcion 2
    print ("Transferencia")
    trans.tipo = " Transferencia Enviada"
def balanceMoneda(): #opcion 3
    print ("Balance de moneda") 
def balanceGeneral(): #opcion 4
    print ("Balance general")
def historicoTrans(): #opcion 5
    print ("Transacciones historicas")
    for trans in lista:
        
        print (trans.fecha,"-",trans.nroT,"-", trans.codID,"-",trans.sym,"-",trans.nom,"-",
        trans.cantCM)

def salir(): #opcion 6
    print ("Gracias por utilizar la aplicación.")

def menu() :
    op = 0
    print("Bienvenido",usuario,"seleccione una opción para continuar: ")
    while op != 6:
        print ("Menu")
        print ("1- Recibir cantidad")
        print ("2- Transferir monto")
        print ("3- Mostrar balance de una moneda")
        print ("4- Mostrar balance general")
        print ("5- Mostrar historico de transacciones")
        print ("6- Salir")
        op = int(input("Ingrese una opción: "))

        if op == 1:            
            recibirCripto()
        elif op == 2:
            transferirMonto()
        elif op == 3:
            balanceMoneda()
        elif op == 4:
            balanceGeneral()
        elif op == 5:
            historicoTrans()
        elif op == 6:
            salir()

i=0
usuario = input("Ingrese su numero de usuario: ")
while not esnumero(usuario):
            cant = input("Ingrese su numero de usuario: ")
            usuario = cant

menu()
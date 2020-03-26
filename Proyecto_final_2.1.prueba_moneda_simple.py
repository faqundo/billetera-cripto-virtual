global lista
lista = [] #es lo mismo que declarar lista= list()


from datetime import date
import requests

class Transacciones:
    symbol = ""
    nombre = ""
    cantCripto = 0.00
    fecha =date.today()
    tipo =""
    codID = 0
    usdTransaccion = 0

usuario = input("Ingrese su numero de usuario: ")

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
def codigoID(codigo):
    return codigo != usuario


def  recibirCripto(): #opcion 1
    criptoT = Transacciones()      
    monedas_dict = {"BTC":"Bitcoin","BCC":"BitConnect","LTC":"Litecoin","ETH":"Ethereum","ETC":"Ethereum Classic","XRP":"XRP"}
    moneda = input(">Ingrese el simbolo de la moneda deseada:\n (BTC,BCC,LTC,ETH,ETC,XRP): " )
    while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda= input(">Ingrese el simbolo de la moneda deseada:\n (BTC,BCC,LTC,ETH,ETC,XRP): ")
    else:
        print("Moneda Valida")
        criptoT.nombre = monedas_dict.get(moneda)
        criptoT.symbol = moneda
    criptoT.cantCripto = float(input(">Ingrese la cantidad a recibir de la criptomoneda: "))
    criptoT.codID = int(input(">Ingrese el codigo del destinatario.")) 

def transferirMonto(): #opcion 2
    print ("Transferencia")
def balanceMoneda(): #opcion 3
    print ("Balance de moneda") 
def balanceGeneral(): #opcion 4
    print ("Balance general")
def historicoTrans(): #opcion 5
    print ("Transacciones historicas")
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
menu()
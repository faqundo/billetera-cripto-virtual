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

monedas = ()

def esmoneda(cripto):
    return cripto in monedas


# monedas_dict = {}
# data=requests.get("https://api.coinmarketcap.com/v2/listings/").json()
# for cripto in data["data"]:
#     monedas_dict[cripto["symbol"]]=cripto["name"]

# monedas = monedas_dict.keys()

# moneda=input("Indique el nombre de la moneda a verificar: ")

while not esmoneda(moneda):        
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:,",moneda,"y nombre:",monedas_dict.get(moneda),
        "es valida porque existe en coimnmarketcap.com")
  

def  recibirCripto(): #opcion 1
    print("Recibir criptomonedas")
    criptoT = Transacciones()      
    criptoT.symbol = input("Ingrese el simbolo de la moneda deseada: (ej:BTC,BCC,LTC,ETH,ETC,XRP...)") 
    monedas = ()
    monedas_dict = {}
    data=requests.get("https://api.coinmarketcap.com/v2/listings/").json()
    for cripto in data["data"]:
        monedas_dict[cripto["symbol"]]=cripto["name"]
    monedas = monedas_dict.keys()  
    moneda=criptoT.symbol    
    while not esmoneda(moneda):        
            print("Moneda Invalida.")
            moneda=input("Ingrese el simbolo de la moneda: ")
    else:
        print("La moneda con symbol:,",moneda,"y nombre:",monedas_dict.get(moneda),
            "es valida porque existe en coimnmarketcap.com")

    criptoT.nombre = str(monedas_dict.get(criptoT.symbol))
    criptoT.cantCripto = float(input("Ingrese la cantidad a recibir de la criptomoneda: "))
    criptoT.codID = int(input("Ingrese el codigo del destinatario.")) 

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
    print("Funcion Menu iniciada")
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
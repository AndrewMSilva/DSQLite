from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
import hashlib
import time
import json

class DSQLiteClient():
	# Host settings
	__Port = 5918
	# Control settings
	__Running = True
	__Socket  = None
	__Connections = {}
	__Timeout     = 0.1
	# Authentication settings
	__Key = None
	# Message settings
	__BufferLength = 1024
	__QueryType    = 0
	__ResponseType = 1

	def __init__(self, ip, key):
		# Hashing keys
		self.__Key = hashlib.sha1(key.encode('latin1')).hexdigest()
		self.__Socket = socket(AF_INET, SOCK_STREAM)
		self.__Socket.connect((ip, self.__Port))
	
	# Enconding a message
	def __EncodeMessage(self, data, type=__QueryType, private=False):
		message = {'type': type,'time_stamp': time.time(), 'key': self.__Key, 'data': data}
		return json.dumps(message.decode('latin1'))
	
	# Receiving and authenticating a message
	def __Receive(self, ip):
		enconded_message = self.__Connections[ip].conn.recv(self.__BufferLength)
		message = json.loads(enconded_message.decode('latin1'))
		if 'key' in message and 'time_stamp' in message and 'data' in message:
			if message.key != self.__PublicKey:
				return
			return message					
		else:
			return
	
	def Execute(self, query):
		try:
			self.__Socket.send(self.__EncodeMessage(query))
		except:
			pass
	
	def Close(self):
		self.__Socket.close()
#TCP server example
import socket
import sys
from _thread import *

HOST = '127.0.0.1'
PORT = 5004

print('Hulti server booting up')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

try:
	server.bind((HOST, PORT))
	print('Socket bind ok ')
except socket.error as msg:
	print('Bind failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
	sys.exit()

server.listen(5)
print('Server listening on: ' + str(HOST) + ':' + str(PORT))

#function that checks the message and allocates it to the 
#appropriate 'tower'
def checkMessage(message):
	if not message: 
		print('message is empty...')
	if 'T0' in message: 
		print('this is a message to tower 0')
	if 'T1' in message: 
		print('this is a message to tower 1')
	if 'T2' in message: 
		print('this is a message to tower 2')
	if 'T3' in message: 
		print('this is a message to tower 3')
		
#function for handling connections. Used to create threads
def clientthread(conn):
	conn.send('Welcome to the void'.encode())
	while True:
		#receive data from the client
		#this is what you need to parse serially

		data = conn.recv(1024)
		checkMessage(data.decode())
		reply = 'Server Received: ' + str(data)
		print('Received: ' + data.decode())
		if not data:
			break
		conn.sendall(reply.encode())
	#loop broken
	conn.close()

while 1: 
	#wait to accept a connection - blocking call
	conn, addr = server.accept()
	print('Connected to client at: ' +addr[0] + ':' + str(addr[1]))

	#start new thread. Takes 1st argument as function name to be run
	start_new_thread(clientthread, (conn,))

server.close()
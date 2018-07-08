#This script goes on the raspberryPi controlling hulti
#TODO:
#1. Add serial and gcode parser
#2. Add logic for gcode
import socket
import time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = '10.0.0.100'
port = 5004
address = (ip,port)
server.bind(address)
print('server running on: ' + ip + ':' + str(port))

#currently only accepting one client
print('only accepting one client')
server.listen(1)
print('listening...')

#accept connection
client , addr = server.accept()
print('Got a connection from ', addr[0],' : ', addr[1])

while True:
    data = client.recv(1024).decode()
    print('Received ', data, ' from the client')
    client.send("Tower 1 Moving".encode())
    time.sleep(1)



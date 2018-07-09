#This script goes on the raspberryPi controlling hulti
#TODO:
#1. Add serial and gcode parser
#2. Add logic for gcode
#3. Sequence it out. Server should always home at the start of a session.
#4. Should server keep track of position and avoid collision? Sketch it out.
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
    try:
        data = client.recv(1024).decode()
        forwardMessage(data)
        print('Received ', data, ' from the client')
        client.send("Tower 1 Moving".encode())
        time.sleep(1)
    except KeyboardInterrupt:
        server.close()
    except:


def forwardMessage(package):
    if(package.find('T0')):
        print('Found T0')



def bootSequence():
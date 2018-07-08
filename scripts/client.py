#this is a preliminary client for testing purpose.
#

import socket

client = socket.socket()
client.connect(('10.0.0.100' , 5004))
message = input(" -> ")

while message != 'q':
    client.send(message.encode())
    data = client.recv(1024).decode()
    print('received from server:' + data)
    message = input(" -> ")
client.close()

if __name__ == '__main__':
    Main()

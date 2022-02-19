
import socket
import time

sock = socket.socket()
# st = input("Ip server:")
st = 'localhost'

try:
	sock.connect((st, 9091))
except:
	print("Connection error!")
	exit()

room = input()

def init():#TODO encoding
    sock.send(room.encode())
    a = sock.recv(4)
    if  a == None:
        exit()

    time.sleep(3)

def function(data_x, data_y):
    sock.send(data_x.to_bytes(2, 'big') + data_y.to_bytes(2, 'big'))

    bata = sock.recv(4)
    bata = [int.from_bytes(bata[:2], byteorder ='big',signed=False),
            int.from_bytes(bata[2:4], byteorder ='big',signed=False)]

    return bata

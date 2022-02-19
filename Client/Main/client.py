
import socket
import time

sock = socket.socket()
st = input("Ip server:")

try:
	sock.connect((st, 9091))
except:
	print("Connection error!")
	exit()

def function(data_x, data_y):
    time.sleep(1)
    sock.send(data_x.to_bytes(2, 'big') + data_y.to_bytes(2, 'big'))
    print(data_x.to_bytes(2, 'big'))
    print(data_y.to_bytes(2, 'big'))

    bata = sock.recv(4)
    bata = [int.from_bytes(bata[:2], byteorder ='big',signed=False),
            int.from_bytes(bata[2:4], byteorder ='big',signed=False)]

    return bata

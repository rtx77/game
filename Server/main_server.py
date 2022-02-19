import socket

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(5)

#first clients connection
conn_1, addr_1 = sock.accept()
conn_2, addr_2 = sock.accept()

while True:
    data_1 = conn_1.recv(4)
    data_2 = conn_2.recv(4)
    conn_1.send(data_2)
    conn_2.send(data_1)

    print(f"{type(data_1)} {data_2}" )
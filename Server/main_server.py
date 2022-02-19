import socket
import time
from threading import Thread

class Network:
    room_pull = []

    @classmethod
    def init(cls):
        cls.sock = socket.socket()
        cls.sock.bind(('', 9091))
        cls.sock.listen(5)
        cls.init_room()

    @staticmethod
    def sortt(room_pull, room_namber):
        for i in room_pull:
            if i[0] == room_namber:
                return i
        return None

    @classmethod
    def init_room(cls):
        while True:
            conn_1, addr_1 = cls.sock.accept()
            room_namber = conn_1.recv(2)
            s = cls.sortt(cls.room_pull, room_namber)
            if s != None:
                cls.room_pull.remove(s)
                # new tread
                conn_1.send(b'\x66')
                s[1].send(b'\x66')
                print("New tread created")
                th = Thread(target=cls.session_connection, args=(conn_1, s[1]))
                th.start()
            else:
                print("New connection")
                cls.room_pull.append(tuple((room_namber, conn_1)))

    @classmethod
    def session_connection(cls, conn_1, conn_2):
        print("newsession")
        while True:
            try:
                data_1 = conn_1.recv(4)
                data_2 = conn_2.recv(4)
                conn_1.send(data_2)
                conn_2.send(data_1)
            except:
                conn_1.close()
                conn_2.close()
                print("session connection error!")
                exit()
# try:
#     Network.init()
# finally:
#     Network.sock.close()
Network.init()
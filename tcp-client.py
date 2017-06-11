# -*- coding: utf-8 -*-

import socket
import datetime

HOST = '0.0.0.0'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(1024)
print('received: ' + str(data))
s.close()
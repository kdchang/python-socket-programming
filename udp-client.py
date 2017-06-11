# -*- coding: utf-8 -*-
import socket 
HOST = '0.0.0.0'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = input('Please keyin your data!')
s.sendto(data.encode(), (HOST, PORT))
print('send {} to {} '.format(data, HOST))
s.close()
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:53:07 2023

@author: shams
"""

import socket


# Partie connexion au canal IRC de root me
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'irc.root-me.org'
PORT = 6697
NICK = 'Salxs'

s.connect((HOST, PORT))

nick_data = ('NICK' + NICK + '\r\n')
s.send(nick_data.encode())

username_data = ('USER Salxs Salxs Salxs :Salxs \r\n ')
s.send(username_data.encode())

s.send('JOIN #root-me \r\n'.encode())

while True :
    result = s.recv(2048).decode('utf-8')
    print(result)
    
    if result[0:4] == "PING":
        s.send(("PONG" + result[4:] + "\r\n").encode())
        
    if len(result)==0:
        break

 
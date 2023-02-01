# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:13:41 2023

@author: User
"""

# Exercice Retour au collège challenge Root me 
# Réalisé cette fois-ci sans utilisation d'une libriarie python pour manipuler le canal IRC

import socket
import math


# Création d'un objet socket pour établir la connexion IRC
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.root-me.org"
channel = "#root-me-challenge"
nick = "Salxs"
botname = "Candy"

def joinChan(chan):
    connexion_serveur.send(bytes("JOIN" + chan + "\n", "UTF-8"))
    ircmsg = ""
    while(ircmsg.find("End of /NAMES list.")==-1):
        ircmsg = connexion_serveur.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.split('\n\r')
        print(ircmsg)
        
def joinServer(server):
    connexion_serveur.connect((server, 6667))
    connexion_serveur.send(bytes("USER "+ nick +" "+ nick +" "+ nick +" :This is a fun bot !\n", "UTF-8"))
    connexion_serveur.send(bytes("NICK"+ nick+"\n","UTF-8"))
    ircmsg = ""
    while(ircmsg.find('MODE Salxs')==-1):
        ircmsg = connexion_serveur.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.split('\n\r')

def sendData(data):
    connexion_serveur.send(data.encode("UTF-8"))

def calcul(nombre1, nombre2):
    nombreModifie = math.pow(nombre1, 2)
    return int(nombre2 * nombreModifie)

#Programme principal

#Je rejoins le serveur et le channel du challenge
joinServer(server)
joinChan(channel)

#Envoie d'un message au bot pour démarrer le challenge 
connexion_serveur.sendData("PRIVMSG"+" "+botname+" "+"!ep1\r\n")

#Récupération du message envoyé par le bot 
while(1):
    msg = connexion_serveur.recv(2048).decode("UTF-8")
    if(msg != ""):
        msg = msg.split("/")
        nombre1 = int(msg[0])
        nombre2 = int(msg[1])
        resultat = str(calcul(nombre1, nombre2))
        sendData("PRIVMSG !ep1 -rep "+resultat)
        break




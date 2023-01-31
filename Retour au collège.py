# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:56:48 2023

@author: Salxs
"""
# Importation des modules utiles
import math
import irclib

#Exercice retour au collège 
def calcul(nombre1, nombre2):
    nombreModifie = math.pow(nombre1, 2)
    return int(nombre2 * nombreModifie)

def on_message(connection, event):
    #Partie réception de message
    message = event.argument[0]
    message_modifie = message.split("/")
    nombre1 = int(message_modifie[0])
    nombre2 = int(message_modifie[1])
    resultat = calcul(nombre1, nombre2)
    


# Configuration du serveur
server = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
nickname ="candy"

#création de la connexion
irc = irclib.IRC()
irc.connect(server, port, nickname)

#rejoindre un canal
irc.join(channel)

#envoyer un message 
irc.privmsg(channel, "!ep1")

#récupération du message
irc.add_global_handler("privmsg", on_message)




import os
import socket
import threading

host = '127.0.0.1'
port = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

used_letters = []


def check_letter(symbol):
    if not isinstance(symbol, str):
        raise TypeError
    if len(symbol) != 1 or ord(symbol) > 90 or ord(symbol) < 65 or symbol in used_letters:
        raise ValueError
    else:
        used_letters.append(symbol)


def handle(client):
    while True:
        word = client.recv(1024)
        try:
            for letter in word:
                check_letter(letter)







        except:
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))


os.system('clear')
receive()



















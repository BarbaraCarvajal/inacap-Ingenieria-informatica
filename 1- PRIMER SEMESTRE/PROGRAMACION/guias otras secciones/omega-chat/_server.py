import socket
import threading
import time as t
from colorama import Fore

HOST = '127.0.0.1'
PORT = 60555

clients = []
usernames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def ChatBrodcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def HandleChatMessages(client):
    while True:
        try:
            message = client.recv(1024)
            ChatBrodcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            ChatBrodcast(f"{Fore.RED}[BOT] Omega: {username} disconnected!{Fore.RESET}".encode('utf-8'), client)
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break

def ReceiveConnections():
    while True:
        client, address = server.accept()

        client.send("@username".encode("utf-8"))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{Fore.GREEN}[BOT] Omega: {username} joined to chat! (Address: {str(address)})")
        message = f"{Fore.GREEN}[JOIN]{Fore.RESET} {username} has joined to chat. Welcome!".encode("utf-8")
        ChatBrodcast(message, client)
        client.send("You were connected to the chat!".encode("utf-8"))

        thread = threading.Thread(target=HandleChatMessages, args=(client,))
        thread.start()

def InitializeServer():
    print(f"{Fore.YELLOW}[OMEGA-SERVER] {Fore.WHITE}Loading chat server wait a moment...")
    t.sleep(3)
    print(f"{Fore.YELLOW}[OMEGA-SERVER] {Fore.WHITE}Server loaded succesfully!")
    ReceiveConnections()

if __name__ == '__main__':
    InitializeServer()
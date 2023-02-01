import socket
import threading
from colorama import Fore
import time as t

username = input(f"{Fore.MAGENTA}[OMEGA-CHAT]{Fore.RESET} > Write your username: ")

IP = '127.0.0.1'
HOST = 60555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, HOST))

def ReceiveMessages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@username":
                client.send(username.encode("utf-8"))
            else: print(message)
        
        except:
            print(f"{Fore.RED}[ERROR] An error was ocurred.")
            client.close()
            break

def WriteMessages():
    while True:
        timestamp = t.strftime("%H:%M:%S")
        message = f"{timestamp} {Fore.MAGENTA}[OMEGA] {Fore.WHITE}<{username}>: {input('')}"
        client.send(message.encode('utf-8'))

def InitializeClient():
    receive_thread = threading.Thread(target=ReceiveMessages)
    receive_thread.start()

    write_thread = threading.Thread(target=WriteMessages)
    write_thread.start()

if __name__ == '__main__':
    print(f"{Fore.MAGENTA}[CHAT] {Fore.WHITE}Initializing client...")
    t.sleep(4)
    InitializeClient()
from socket import socket, AF_INET, SOCK_STREAM

IP = '127.0.0.1'
HOST = 60555

if __name__ == '__main__':
    username = input("> Write your username: ")
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((IP, HOST))

    client.send(username.encode("utf-8"))

    while True:
        message = input(f"> ")
        client.send(message.encode("utf-8"))
        print(f"> {message}")
        if message == "exit":
            break
        message = client.recv(1024).decode("utf-8")
        print(f"< {message}")
    client.close()
    print("Bye!")

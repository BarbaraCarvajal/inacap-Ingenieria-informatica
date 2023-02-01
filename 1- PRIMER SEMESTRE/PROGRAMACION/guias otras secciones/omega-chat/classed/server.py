from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
"""
    This script uses google docstring to get the description of the functions.
    https://google.github.io/styleguide/pyguide.html

    Script by @manucabral
    Original code by @le01q
"""

class OmegaClient:
    """
        Omega client class.
        This class is used to create a client object.

        Args:
            username (str): The username of the client.
            socket (socket): The socket of the client.
            address (tuple): The address of the client.
        
        Returns: 
            None
    """
    def __init__(self, username: str, socket: socket, address: tuple):
        self.username = username
        self.socket = socket
        self.address = address
        self.number_of_messages = 0

    def __str__(self):
        """
            Returns the string representation of the object
                
            Args:
                None
        
            Returns:
                The string representation of the object
        
            Raises:
                None
        """
        return f"OmegaClient(username={self.username}, address={self.address})"
    
    def get_message(self):
        """
            Gets the message from the client.
                
            Args:
                None
        
            Returns:
                The message from the client
        
            Raises:
                None
        """
        self.number_of_messages += 1
        return self.socket.recv(1024).decode('utf-8')
    
    def send_message(self, message: str):
        """
            Sends a message to the client.
                
            Args:
                message (str): The message to send.
        
            Returns:
                None
        
            Raises:
                None
        """
        self.socket.send(message.encode('utf-8'))
    
class Omega:
    """
    Omega Chat Server

    Args:
        host (str): The host of the server (default: localhost)
        port (int): The port of the server (default: 60555)

    Returns:
        None

    Raises:
        Exception: An error was ocurred while creating the server socket
    """
    def __init__(self, host: str = "localhost", port: int = 60555, max_clients: int = 10):
        try:
            self.server = socket(AF_INET, SOCK_STREAM)
        except Exception as e:
            self.log(f"An error was ocurred while creating the server socket {e}", "ERROR")
            exit()
        self.address = host, port
        self.max_clients = max_clients
        self.clients = self.message = []


    def log(self, message: str, type: str = "INFO"):
        """
            Logs a message to the console
            
            Args:
                message (str): The message to log
                type (str): The type of the message (default: INFO)
    
            Returns:
                None
    
            Raises:
                Exception: An error was ocurred while logging the message
        """
        try:
            print(f"[{type}] {message}")
        except Exception as e:
            print(f"[ERROR] An error was ocurred while logging the message {e}")

    def start(self):
        """
            Starts the server
                
            Args:
                None
        
            Returns:
                None
        
            Raises:
                Exception: An error was ocurred while starting the server
                KeyboardInterrupt: The user pressed Ctrl+C to stop the server
        """
        try:
            self.server.bind(self.address)
            self.server.listen(self.max_clients)
            self.log(f"Server started on {self.address}")
            self.receive_clients()
        except Exception as e:
            self.log(f"An error was ocurred while starting the server {e}", "ERROR")
            return False

    def receive_clients(self):
        """
            Receives clients
                
            Args:
                None
        
            Returns:
                True if the clients were received successfully. False otherwise.
        
            Raises:
                Exception: An error was ocurred while receiving the clients
        """
        try:
            while True:
                client_socket, client_address = self.server.accept()
                client = OmegaClient("undefined", client_socket, client_address)
                self.clients.append(client)
                self.log(f"Client {client.username} connected to the server")
                Thread(target=self.handle_client, args=(client,)).start()
        except Exception as e:
            self.log(f"An error was ocurred while receiving the clients {e}", "ERROR")
            return False

    def handle_client(self, client: OmegaClient):
        """
            Handles a client
                
            Args:
                client (socket): The client to handle
        
            Returns:
                None
        
            Raises:
                Exception: An error was ocurred while handling the client
        """
        try:
            while True:
                message = client.get_message()
                if not message:
                    self.log(f"Client {client.username} disconnected")
                    self.clients.remove(client)
                    break
                elif message == "exit":
                    self.log(f"Client {client.username} disconnected")
                    self.clients.remove(client)
                    break
                elif client.number_of_messages == 1:
                    self.log(f"Client {client.username} now is known as {message}")
                    client.username = message
                else: 
                    self.log(f"{client.username}: {message}")
                    self.send_message(message)
                    
        except Exception as e:
            self.log(f"An error was ocurred while handling the client {e}", "ERROR")

    def send_message(self, message: str):
        """
            Sends a message to all the clients
                
            Args:
                message (bytes): The message to send
        
            Returns:
                None
        
            Raises:
                Exception: An error was ocurred while sending the message
        """
        try:
            for client in self.clients:
                client.send_message(message)
        except Exception as e:
            self.log(f"An error was ocurred while sending the message {e}", "ERROR")
        
if __name__ == "__main__":
    omega = Omega()
    omega.start()
    omega.log("Server stopped")
    exit()
import socket
import threading

#if server is online so provide private ip add here
host='127.0.0.1'
port=8501

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients = []
nicknames = []

#broadcast-sends a message to all connected clients
def broadcast(message):
    for client in clients:import socket
import threading

#if server is online so provide private ip add here
host='127.0.0.1'
port=9000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients = []
nicknames = []

#broadcast-sends a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)
#receive-listens from clients and accpets new connections from clients(first client is connected here)it runs in the main thread its the first func well call
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # print(f"{names[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            #then end this thread
            break
            #error(client disconnects or crashes i want to remove it from the nicknames list and the clients list)




def receive():
    while True:
        client, address = server.accept()
        #accept method returns client socket
        print(f"connected with {str(address)}!")
        #add client to clients list
        #client socket has keyword signals to the client that im sending the nickname
        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024)
        #receive from client his name and append it to names
        nicknames.append(nickname)
        clients.append(client)
        print(f"Name of client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('ascii'))
        client.send("connected to the server".encode('ascii'))
        thread=threading.Thread(target=handle, args=(client,))
        thread.start()

print("server running")
receive()
#handle-handles individual connections from the client(second client is handled here)import socket
import threading

#if server is online so provide private ip add here
host='127.0.0.1'
port=9000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients = []
nicknames = []

#broadcast-sends a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)
#receive-listens from clients and accpets new connections from clients(first client is connected here)it runs in the main thread its the first func well call
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # print(f"{names[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            #then end this thread
            break
            #error(client disconnects or crashes i want to remove it from the nicknames list and the clients list)




def receive():
    while True:
        client, address = server.accept()
        #accept method returns client socket
        print(f"connected with {str(address)}!")
        #add client to clients list
        #client socket has keyword signals to the client that im sending the nickname
        client.send("NICK".encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        #receive from client his name and append it to names
        nicknames.append(nickname)
        clients.append(client)
        print(f"Name of client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('ascii'))
        client.send("connected to the server".encode('ascii'))
        thread=threading.Thread(target=handle, args=(client,))
        thread.start()

print("server running")
receive()
#handle-handles individual connections from the client(second client is handled here)import socket
import threading

#if server is online so provide private ip add here
host='127.0.0.1'
port=9000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients = []
nicknames = []

#broadcast-sends a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)
#receive-listens from clients and accpets new connections from clients(first client is connected here)it runs in the main thread its the first func well call
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # print(f"{names[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            #then end this thread
            break
            #error(client disconnects or crashes i want to remove it from the nicknames list and the clients list)




def receive():
    while True:
        client, address = server.accept()
        #accept method returns client socket
        print(f"connected with {str(address)}!")
        #add client to clients list
        #client socket has keyword signals to the client that im sending the nickname
        client.send("NICK".encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        #receive from client his name and append it to names
        nicknames.append(nickname)
        clients.append(client)
        print(f"Name of client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('ascii'))
        client.send("connected to the server".encode('ascii'))
        thread=threading.Thread(target=handle, args=(client,))
        thread.start()

print("server running")
receive()
#handle-handles individual connections from the client(second client is handled here)import socket
import threading

#if server is online so provide private ip add here
host='127.0.0.1'
port=9000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()

clients = []
nicknames = []

#broadcast-sends a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)
#receive-listens from clients and accpets new connections from clients(first client is connected here)it runs in the main thread its the first func well call
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            # broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            #then end this thread
            break
            #error(client disconnects or crashes i want to remove it from the nicknames list and the clients list)




def receive():
    while True:
        client, address = server.accept()
        #accept method returns client socket
        print(f"connected with {str(address)}!")
        #add client to clients list
        #client socket has keyword signals to the client that im sending the nickname
        client.send("NICK".encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        #receive from client his name and append it to names
        nicknames.append(nickname)
        clients.append(client)
        print(f"Name of client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("connected to the server".encode('utf-8'))
        thread=threading.Thread(target=handle, args=(client,))
        thread.start()

print("server running")
receive()
#handle-handles individual connections from the client(second client is handled here)

#receive-listens from clients and accpets new connections from clients(first client is connected here)it runs in the main thread its the first func well call

#handle-handles individual connections from the client(second client is handled here)

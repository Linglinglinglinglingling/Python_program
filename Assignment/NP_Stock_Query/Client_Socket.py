from socket import *
chosen_index=""
serverName = 'localhost'
serverPort = 12000
## create client socket, first argument indicates IPv4, second argument means it is TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#client establish TCP connection
clientSocket.connect((serverName,serverPort))

#Client receive packet from server
menu = clientSocket.recv(2048)
print(menu.decode())
while chosen_index!="q":
    valid_input=False
    while not(valid_input):
        chosen_index=input("please input the item number here or press 'q' to disconnect: ")
        chosen_index=chosen_index.strip()
        if chosen_index in ["1","2","3","4","q"]:
            valid_input=True

    if chosen_index!="q":
        clientSocket.send(chosen_index.encode())
        query_result = clientSocket.recv(2048).decode()
        print(query_result)
    else:
        clientSocket.send(chosen_index.encode())
        clientSocket.close()
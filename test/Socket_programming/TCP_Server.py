from socket import *
serverPort = 12000
#Create server socket
serverSocket = socket(AF_INET,SOCK_STREAM)
#Associate the port number with the socket
serverSocket.bind(('118.138.116.43',serverPort))
#Maximum connection is 1
serverSocket.listen(2)
print( "The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
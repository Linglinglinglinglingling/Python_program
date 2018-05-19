from socket import *
from Assignment.NP_Stock_Query.Server_function import Stock_Server

import time
#
class Connection:
    def __init__(self):
        self.server=Stock_Server()

    #accessor
    def get(self):
        pass

    #mutator
    def set(self):
        pass


    def show_menu(self):
        menu_message="Below is the stock menu, please choose the item number you would like to query"+ "\n"
        menu_message+=str(self.server)
        return menu_message

    # Send both the result and newest menu info
    def show_query(self,index):
        red="\033[31m"
        white="\033[0m"
        query_result="\n"+red+"Here is the result"+"\t"+self.server.stock_query(index)\
                     + "\n"+"\n"+white+self.show_menu()
        return query_result

    def provide_service(self,socketname):

        while True:
            try:
                chosen_index = ""
                connectionSocket, addr = socketname.accept()
                print("establish connection with " + str(addr))
                # sentence = connectionSocket.recv(1024).decode()
                connectionSocket.send(self.show_menu().encode())
                while chosen_index != "q":
                    chosen_index = connectionSocket.recv(1024).decode()
                    if chosen_index != "q":
                        connectionSocket.send(self.show_query(int(chosen_index)).encode())
                    else:
                        connectionSocket.close()
                        print("connection with " + str(addr) + " closed")
            except:
                continue

    def __str__(self):
        pass

    def __contains__(self, item):
        pass

def main():
    new_connection=Connection()
    serverPort = 12000
    # Create server socket

    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Associate the port number with the socket
    serverSocket.bind(('localhost', serverPort))
    # Maximum connection is 2
    serverSocket.listen(2)
    print("The server is ready to receive")
    new_connection.provide_service(serverSocket)


    # while True:
    #     chosen_index = ""
    #     connectionSocket, addr = serverSocket.accept()
    #     print("establish connection with "+str(addr))
    #     # sentence = connectionSocket.recv(1024).decode()
    #     connectionSocket.send(new_connection.show_menu().encode())
    #     while chosen_index!="q":
    #         chosen_index=connectionSocket.recv(1024).decode()
    #         if chosen_index!="q":
    #             connectionSocket.send(new_connection.show_query(int(chosen_index)).encode())
    #         else:
    #             connectionSocket.close()
    #             print("connection with "+str(addr)+" closed")



if __name__ == '__main__':
    main()








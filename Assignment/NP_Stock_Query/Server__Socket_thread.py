from socket import *
from Assignment.NP_Stock_Query.Server_function import Stock_Server
import threading
import time


#
class Connection:
    def __init__(self):

        self.server = Stock_Server()

        self.serverPort = 12000
        # Create server socket

        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # Associate the port number with the socket, and enable the socket can be reused
        self.serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.serverSocket.bind(('localhost', self.serverPort))
        # Maximum connection is 2

    def listen(self):
        self.serverSocket.listen(2)
        print("The server is ready to receive")
        while True:
            connectionSocket, addr = self.serverSocket.accept()
            try:
                threading.Thread(target=self.provide_service, args=(connectionSocket, addr)).start()
            except:
                continue

    def show_menu(self):
        menu_message = "Below is the stock menu, please choose the item number you would like to query" + "\n"
        menu_message += str(self.server)
        return menu_message

    # Send both the result and newest menu info
    def show_query(self, index):
        red = "\033[31m"
        white = "\033[0m"
        query_result = "\n" + red + "Here is the result" + "\t" + self.server.stock_query(index) \
                       + "\n" + "\n" + white + self.show_menu()
        return query_result

    def provide_service(self, connectionSocket, addr):
        while True:
            chosen_index = ""

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
                    return None
    def __str__(self):
        pass

    def __contains__(self, item):
        pass


def main():
    a = Connection()
    a.listen()



if __name__ == '__main__':
    main()

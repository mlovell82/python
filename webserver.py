# this code written by Dr. Jong Hoon Kim

from socket import *

serverPort = 12000      # an int variable representing a port
ServerSocket = socket(AF_INET, SOCK_STREAM)     # list with 2 strings (SOCK_STREAM is for TCP, AF_INET defines web based instead of packet based
serverSocket.bind(('',serverPort))              # bind is a function with 2 parameters port and address
serverSocket.listen(1)                          # how many clients do you want at a time
clientlist = []                                 # empty list
print("the server is ready to receive")
while true:
    print("...step 01")
    connectionSocket, addr = serverSocket.accept()  # accept() waits for client connectionSocket is a portal between server and client
    sentence = connectionSocket.recv(1024).decode() # listen to client request and assign it to sentence
    capitalizedSentence = sentence.upper()          # makes everything from sentence uppercase
    connectionSocket.send(capitalizedSentence.encode()) # make into a byte stream and a bit to encrypt; on otherside bit removed
    connectionSocket.close() # send back to client
    print("done")

    ''' needed for assignment
            1.  create a connection socket when contacted by a client (browser)
            2.  receive the HTTP request from this connection
            3.  parse the request to determine the specific file being requested
            4.  get the requested file from the server’s file system
            5.  create an HTTP response message consisting of the requested file preceded by header lines;and
            6.  send the response over the TCP connection to the requesting browser. If a browser requests a file that is not present in your server, your server should return a“404 Not Found” error message'''

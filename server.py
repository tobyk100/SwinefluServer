import socket

s = socket.socket()
host = 'localhost'
port = 27015
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)
while True:
    #try:
        client, address = s.accept()
        print 'Connected by', address
        while True:
            data = client.recv(size)
            print data
            client.send(data)
    #except:
     #   print "Connection to client lost."
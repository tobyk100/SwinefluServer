import socket, parselogs

s = socket.socket()
host = 'localhost'
port = 27015
size = 1024
logfile = 'capture.log'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)
while True:
    client, address = s.accept()
    print 'Connected by', address
    if True:
        data = client.recv(size)
        with open(logfile, "a") as logfd:
            logfd.write(data)
        client.send(data)
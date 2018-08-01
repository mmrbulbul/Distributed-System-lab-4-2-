#server 
import socket

sock = socket.socket()
print "socket created"

port = 22336

sock.bind(('',port))
print "socket binded to %s" %(port)

sock.listen(1)
print "server is listening"

while True:
    client, addr = sock.accept()
    print "connection request from",addr
    while True:
        request = client.recv(4096)
        if (request == "BEGIN"):
            client.send("Acknowledged")
            while True:
                echo = client.recv(4096)
                client.send(echo)
                if(echo == "END"):
                    break
        else:
            continue
        break
    print "Connection closed with",addr
    client.close()
             
            
#client side
import socket,sys

s = socket.socket()
port= int(sys.argv[1])
localhost = "127.0.0.1"
s.connect((localhost, port))
flag=True	
while True:
	
	reply = s.recv(4096)
	if(reply.lower()=="end"):
		print "Connection closed"
		s.close()
		break
	print reply
	request = raw_input()
	s.send(request)
    

# -*- coding: utf-8 -*-
import threading
class server(threading.Thread):

	def __init__(self,client, addr):
		threading.Thread.__init__(self)
		self.client = client
		self.addr = addr

	
	def run(self):
	
		vocub = [ {"server1":"Knock knock!","client1":"Who's there?","server2": "Turnip" , "client2":"Turnip who?" ,"server3": "Turnip the heat. It's freezing.","server":"Would you like to listen to another? (Y/N)"} , 
	
			  {"server1":"Knock knock!","client1":"Who's there?","server2": "Egg" , "client2":"Egg who?" ,"server3": "Eggcited to meet you.","server":"Would you like to listen to another? (Y/N)"} ,
			  
			  {"server1":"Knock knock!","client1":"Who's there?","server2": "Robin" , "client2":"Robin who?" ,"server3": "Robin you! Handover your cash!","server":"Would you like to listen to another? (Y/N)"} ,
			  
			  {"server1":"Knock knock!","client1":"Who's there?","server2": "Butter" , "client2":"Butter who?" ,"server3": "I'll butter tell you few more knock knock jokes","server":"Would you like to listen to another? (Y/N)"} ,
			  
			    {"server1":"Knock knock!","client1":"Who's there?","server2": "Ice Cream" , "client2":"Ice Cream who?" ,"server3": "Ice Cream. If you don't let me in.","server":"Would you like to listen to another? (Y/N)"} ,
			  
			    {"server1":"Knock knock!","client1":"Who's there?","server2": "Barbie" , "client2":"Barbie who?" ,"server3": "Barbie Q Chicken","server":"Would you like to listen to another? (Y/N)"} ,
			     {"server1":"Knock knock!","client1":"Who's there?","server2": "Robin" , "client2":"Robin who?" ,"server3": "Robin you! Handover your cash!","server":"Would you like to listen to another? (Y/N)"} ,
			         {"server1":"Knock knock!","client1":"Who's there?","server2": "Annie" , "client2":"Annie who?" ,"server3": "Annie thing you can do , I can do better.","server":"Would you like to listen to another? (Y/N)"} ,
			         {"server1":"Knock knock!","client1":"Who's there?","server2": "Radio" , "client2":"Radio who?" ,"server3": "Radi o or not I am coming in.","server":"Would you like to listen to another? (Y/N)"} ,
			         
			          {"server1":"Knock knock!","client1":"Who's there?","server2": "Justin" , "client2":"Justin who?" ,"server3": "Justin time for dinner.","server":"Would you like to listen to another? (Y/N)"} ]
	
		import random
		#joke_no = random.randint(0,N-1)
	
		listed = [ False for i in range(10)] # list of listened joke
		#client, addr = sock.accept()
		flag = False 
		close = False
		print "connection request from",self.addr
		while True:
			if(close):
				break
			joke_no = random.randint(0,9)
			if(not listed[joke_no]):
				listed[joke_no] = True
			else:
				continue
			i=1
			while i<=4 :
				if(i==4):
					self.client.send("\n"+vocub[joke_no]["server"])
					request = self.client.recv(4096)
					if(request=="Y"):
						flag = True # want to listen another joke
						break
					else:
						print "Connection closed with",self.addr
						self.client.send("End")
						self.client.close()
						close = True  # connection is closed 
						break 
					
					
				else:
					self.client.send(vocub[joke_no]["server"+str(i)])
					if(i==3):
						i=i+1 
						continue
					request = self.client.recv(4096)
					if(request.lower() != vocub[joke_no]["client"+str(i)].lower()):
						 message= "You are supposed to say, "+ vocub[joke_no]["client"+str(i)] +" Let\’s try again.\n" #"You are supposed to say, "+ vocub[joke_no]["client"+str(i)]+ " Let’s try again."
						 self.client.send(message)
						 i=1
					else:
						i= i+1
				
				
				
		
			
		"""	request = client.recv(4096)
			client.send(request)
			if(request == "END"):
				break    
		print "Connection closed with",addr
		client.close()"""
		
		
    
    

import threading
import socket,sys
sock = socket.socket()
print "socket created"
port = int(sys.argv[1])
sock.bind(('',port))
print "socket binded to %s" %(port)
sock.listen(1)
print "server is listening"	
tst =[]
"""for i in range(5):
	tst.append(server())
	tst[i].start()"""
i=0
while True:
	client, addr = sock.accept()
	tst.append(server(client,addr))
	tst[i].start()
	i=i+1
	
	
	
		

             
            

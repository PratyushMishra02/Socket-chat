import socket 
import sys
import time

s=socket.socket()

host=socket.gethostname()
print("Server will start on host:",host)
port=1234
s.bind((host,port))
print("Server is bound successfully")
s.listen(1)
conn,addr=s.accept()
print(addr,"has connected")
while 1:
    message=input(str("You:>>"))
    message=message.encode()
    conn.send(message)
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    print("Client:>>",incoming_message)

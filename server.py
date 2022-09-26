import socket
import threading
import pickle
from gameclasses import Player,Bullet

host = '192.168.18.58'
port = 9090

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

print('server started')
server.listen(2)

playerobj=[Player((0,0,250),50,50),Player((255,0,0),300,300)]
globalbulls=[0,0]

def handleClient(conn,playernumber):
    conn.send(pickle.dumps(playerobj[playernumber]))
    print(f'{playernumber}connected')
    while True:
        obj=pickle.loads(conn.recv(2048))
        if obj:
            playerobj[playernumber]=obj
            if playernumber==0:
                try:
                    conn.send(pickle.dumps(playerobj[1]))
                except:
                    pass
            if playernumber==1:
                try:
                    conn.send(pickle.dumps(playerobj[0]))
                except:
                    pass
            print(playerobj[playernumber].posx)
        



playernumber=0

while True:
    conn, addr = server.accept()
    thread=threading.Thread(target=handleClient,args=(conn,playernumber))
    thread.start()
    playernumber+=1
    
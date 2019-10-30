import os
import binascii
import base64
import hashlib
from flask import Flask, send_from_directory
from flask import request
from flask import make_response
from flask import Blueprint
from flask import redirect
from flask_cors import CORS
import sys
import base64
import time
import hmac

app = Flask(__name__)
CORS(app)

from flask_uwsgi_websocket import GeventWebSocket
websocket = GeventWebSocket(app)

N = int("EEAF0AB9ADB38DD69C33F80AFA8FC5E86072618775FF3C0B9EA2314C9C256576D674DF7496EA81D3383B4813D692C6E0E0D5D8E250B98BE48E495C1D6089DAD15DC7D7B46154D6B6CE8EF4AD69B15D4982559B297BCF1885C529F566660E57EC68EDBC3C05726CC02FD4CBF4976EAA9AFD5138FE8376435B9FC61D2FC0EB06E3",16)
G = 2
NUMBER_LENGTH = 32
PASSWORD = "correct horse battery staple"

def random_number():
    return btoi(os.urandom(NUMBER_LENGTH))

class SRP:
    STATE_INIT = 0
    STATE_SENT_SALT = 1
    STATE_SENT_B = 2
    STATE_END = 3

    def __init__(self,socket):
        self.state =  SRP.STATE_INIT
        self.socket = socket
        self.salt = btoi(os.urandom(NUMBER_LENGTH))
        print("[+] Salt : " + str(self.salt), file=sys.stdout)

    def serve(self):
        while True:
            message = self.socket.receive()
            if message == None:
                break 

            try:
                m = message.decode('utf-8')
                if m.strip() == "":
                    continue
                self.process(m)
            except Exception as e:
                print("Exception", e)
                print("Resetting to initial state...")
                raise e

    def process(self,message):
        if self.state == SRP.STATE_INIT:
            # receive username
            self.user = message
            
            # send salt
            self.send(itob(self.salt))

            # get ready for next state
            self.state = SRP.STATE_SENT_SALT

        elif self.state == SRP.STATE_SENT_SALT:
            ## receive client's A
            self.A = btoi(binascii.unhexlify(message))

            if self.A % N == 0:
                self.socket.send("Is it me or you are trying to do something nasty here and send me A=0?")
                self.state = SRP.STATE_INIT

            print("[+] received A : " + str(self.A), file=sys.stdout)

            # compute v
            self.compute_v()
            self.b = random_number()
            interm = pow(G, self.b, N)
            self.B = (self.v + interm) % N
               
            # self.B = (self.verifier + pow(G,self.b,N)) % N
            # self.B = (self.verifier + G**self.b) % N
            # self.B = (self.verifier + expmod(G,self.b,N)) % N
            print("[+] sent B : " + str(self.B), file=sys.stdout)
            self.send(itob(self.B))
            self.compute_u()
            self.compute_secret()
            self.state = SRP.STATE_SENT_B                
        
        elif self.state == SRP.STATE_SENT_B:
            # receive hash of the shared secret
            hashed = binascii.unhexlify(message)
            
            # compare 
            h = hashlib.sha256()
            h.update(itob(self.A))
            h.update(itob(self.B))
            h.update(itob(self.S))
            digested = h.digest()
            s = ""
            if digested == hashed:
                s = "Success! "
            else:
                s = "Failure. Hash don't match."
            self.socket.send(s)
            self.state = SRP.STATE_END

    def send(self,msg):
        self.socket.send(binascii.hexlify(msg).decode('utf-8'))

    def send_error(self):
        self.socket.send("error")

    def compute_secret(self):
        # S = (A * v^u) ^ b % N
        self.S = pow((self.A * pow(self.v,self.u,N)),self.b,N)
        
        # self.S = (self.A * self.verifier**self.u) ** self.b
        # self.S = self.S % N

        #self.S = expmod(self.A * expmod(self.verifier,self.u,N),self.b,N)
        print("[+] Secret: : " + str(self.S), file=sys.stdout)

    def compute_u(self):
        h = hashlib.sha256()
        h.update(itob(self.A))
        h.update(itob(self.B))
        self.u = btoi(h.digest())
        print("[+] u : " + str(self.u), file=sys.stdout)

    def compute_v(self):
       inner = hashlib.sha256()
       inner.update(self.user.encode())
       inner.update(":".encode())
       inner.update(PASSWORD.encode())
       print("[+] H(U || \":\" || PASSWORD) => " + binascii.hexlify(inner.digest()).decode(), file=sys.stdout)

       h = hashlib.sha256()
       h.update(itob(self.salt))
       h.update(inner.digest())
       print("[+] H(salt || H(U || \":\" || PASSWORD)):" + binascii.hexlify(h.digest()).decode(), file=sys.stdout)
       x = btoi(h.digest())
       print("[+] x : " + str(x), file=sys.stdout)
       self.v = pow(G,x,N)
       print("[+] v: " + str(self.v), file=sys.stdout)
 
def itob(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def btoi(xbytes):
    return int.from_bytes(xbytes, 'big')

@websocket.route("/")
def websocket_handler(socket):
    srp = SRP(socket)
    srp.serve()

if __name__ == '__main__':
    app.run()
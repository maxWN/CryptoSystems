__author__ = 'Max W.N.'

import sys
from socket import socket
#from Crypto.PublicKey import RSA
import math


sock = socket()
sock.connect(('localhost', 12300))
#The socket connects to port number 12321
print("Connection successfully established.")
print("Enter a phrase without spaces seperating words for proper results.")
entered = sys.argv[1]

#print("Caesar Cipher Encyption:")
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cba=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
caesar=""
x = []
x = entered
track = 0
while(track != len(entered)):
    y=0
    while(y != len(abc)):
        if(x[track]==abc[y]):
            #swap=x.replace(x[track],cba[y])
            caesar+=cba[y]
        # elif(x[track]==' '):
        #     caesar+=' '
        #     y=y+1
        y=y+1
    track=track+1
#lowercase letters in ASCII code are represented by 97-122, and uppercase is represented by 65-90
#

#Double Transposition Encryption:
#x=0
#y=0
#table= [x][y]
#

#RSA Encryption:
###enter a number for RSA to function appropriately...
# C=len(entered)
# value = math.pow(C, e)
# N = (101)*(37)
# e = 1993
# C=(value % N)
# output=C
#
print("Our input after encryption: " + caesar);
packet = caesar.encode("UTF-8")
sock.send(packet)

buff = sock.recv(2048)
item=buff.decode()

print("Output from our decryption server is: " + item)
sock.close()
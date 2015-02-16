__author__ = 'Max W.N.'


import math
from socket import socket

listening = socket()
listening.bind(('localhost', 12300))
listening.listen(5) #the argument is the amount of room our backlog has for cluttered requests!
print("Establishing connection.")

(conn, address) = listening.accept()
print("Connection established.", conn, address)
#space will be used to call functions!

buffer = conn.recv(2048)

print("Received: ", buffer)

decoded = buffer.decode()

print("Decoded: " + decoded)

#Caesar Cipher Decryption Method:######################################################################################
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cba=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
caesar=""
x = []
x = decoded
track = 0
while(track != len(decoded)):
    y=0
    while(y != len(abc)):
        if(x[track]==cba[y]):
            #swap=x.replace(x[track],cba[y])
            caesar+=abc[y]
        # elif(x[track]==' '):
        #     caesar+=' '
        #     y=y+1
        y=y+1
    track=track+1
#######################################################################################################################




#Double Transposition Decryption Method:###############################################################################
# cNumber = math.ceil(len(decoded) / k)
# rNumber = k
# pText = [""] * cNumber
# column = 0
# rows = 0
# for x in decoded:
#     pText[column] += x
#     column += 1
#     if (column == cNumber) or (cNumber == cNumber - 1 and rows >= rNumber - emptyCells):
#         column = 0
#         rows += 1
#######################################################################################################################



#print("RSA Decryption Method:")###############################################################################
# m = len(decoded)
# p = 101
# q = 37
# n=101*37
# N = (101-1)*(37-1)
# e = 1993
# d = math.pow(e, -1) % (N)
#######################################################################################################################


output=caesar

conn.send(output.encode())
conn.close()
listening.close()   #ends the connection.

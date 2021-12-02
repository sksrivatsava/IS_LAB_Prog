import math

p=3                                                                                                             
q=5

n=p*q
print("the n value is ",n)
phi=(p-1)*(q-1)
print("the phi(n) value is ",phi)
e=2

while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e+=1

print("The public key is (",e,",",n,")",sep="")
k=2
for i in range(10):
    x=1+(i*phi)
    if(x%e==0):
        d=x//e
        break


    
print("The private key is (",d,",",n,")",sep="")

msg=3
print("the message data is ",msg)

c=int(pow(msg,e,n))



print("encrypted data is ",c)
m=int(pow(c,d,n))

print("decrypted data is",m)

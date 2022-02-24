import math

#p = 5
#q = 13
#m = 2

p = int(input("\nEnter the value of p.\n"))
q = int(input("\nEnter the value of q.\n"))
m = int(input("\nEnter the numerical message to be sent.\n"))

n = p*q
phi = (p-1)*(q-1)

depairs = []

for i in range(2,phi):
    if math.gcd(n,i)==1:
        for j in range(2,i):
            if (i*j)%phi==1 and i!=j:
                depairs.append((i,j))
                
print("The number of d,e pairs available :\n",depairs)

e = depairs[0][0]
d = depairs[0][1]

print("Message before encryption : {}".format(m))

enc = (m**d)%n
print("Message after encryption : {}".format(enc))

dec = (enc**e)%n
print("Message after decryption : {}".format(dec))

if m == dec :
    print("success")
else:
    print("not success")


        

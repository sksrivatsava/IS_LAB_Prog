s=input()
k=list(input())
kl=len(k)
k1=k.copy()
k1.sort()

ind=[]
for i in k1:
    ind.append(k.index(i))

c=0
et=[]
while c<len(s):
    x=[]
    for i in range(kl):
        if c<len(s):
            x.append(s[c])
            c=c+1
        else:
            x.append(" ")
    et.append(x)

for i in et:
    print(i)
row=len(et)

encry=""

for i in ind:
    for j in range(row):
        encry+=et[j][i]
print(encry)

dt=[[" " for j in range(kl)]for i in range(row)]

c=0
for i in ind:
    for j in range(row):
        dt[j][i]=encry[c]
        c=c+1
decry=""
for i in dt:
    print(i)
    decry+=''.join(i)
print(decry.strip())







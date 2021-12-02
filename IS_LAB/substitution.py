s=input()

k=int(input())

ans=""

for i in s:
    if i.islower():
        ans=ans+chr(((ord(i)-97)+k)%26+97)
    elif i.isupper():
        ans=ans+chr(((ord(i)-65)+k)%26+65)
    elif i.isdigit():
        ans=ans+chr(((ord(i)-48)+k)%10+48)
    else:
        ans=ans+i
print("encrypted",ans)

s=""
for i in ans:
    if i.islower():
        s=s+chr(((ord(i)-97)-k)%26+97)
    elif i.isupper():
        s=s+chr(((ord(i)-65)-k)%26+65)
    elif i.isdigit():
        s=s+chr(((ord(i)-48)-k)%10+48)
    else:
        s=s+i

print("decrypted",s)

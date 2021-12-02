from des import DesKey

key=DesKey(b"some key")
print("key:",key._DesKey__encryption_key)
s=input("enter a text: ")
c=key.encrypt(s.encode(),padding=True)
print("encrypted",c)
d=key.decrypt(c,padding=True)
print("decrypted",d.decode())


from random import randint
 
if __name__ == '__main__':
 
    # Both the persons will be agreed upon the
    # public keys G and P
    # A prime number P is taken
    q = 23
     
    # A primitive root for P, G is taken
    alpha = 9
     
      
    print('The Value of q is :%d'%(q))
    print('The Value of alpha is :%d'%(alpha))
     
    # Alice will choose the private key a
    xa = 4
    print('The Private Key a for Alice is :%d'%(xa))
     
    # gets the generated key
    ya = int(pow(alpha,xa,q))
    print('The Public Key a for Alice is :%d'%(ya))
     
    # Bob will choose the private key b
    xb = 3
    print('The Private Key b for Bob is :%d'%(xb))
    
    # gets the generated key
    yb = int(pow(alpha,xb,q)) 
     
    print('The Public Key b for Bob is :%d'%(yb))
    # Secret key for Alice
    kab = int(pow(yb,xa,q))
     
    # Secret key for Bob
    kba = int(pow(ya,xb,q))
     
    print('Secret key for the Alice is : %d'%(kab))
    print('Secret Key for the Bob is : %d'%(kba))

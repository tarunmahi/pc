import random

def millertest(n,k=20):
    if n==2 or n==3:
        return True
    if n<1 or n%2==0:
        return False
    r,d=0,n-1
    while d%2==0:
        d//=2
        r+=1
    
    for _ in range(k):
        a=random.randint(2,n-2)
        x=pow(a,d,n)
        if x==n-1 or x==1:
            continue
        for _ in range(r-1):
            x=pow(x,2,n)
            if x==n-1:
                break
        else:
            return False
    return True
        
    

def generate_prime(bits):
    while True:
        rand_num=random.getrandbits(bits)
        rand_num|=(1<<bits-1)|1
        if millertest(rand_num):
            return rand_num

def ext_gcd(a,b):
    if a==0:
        return b,0,1
    x0,x1=0,1
    y0,y1=1,0
    while b!=0:
        q,a,b=a//b,b,a%b
        x0,x1=x1-q*x0,x0
        y0,y1=y1-q*y0,y0
    return a,x1,y1
    

def mod_inv(a,b):
    gcd,x,y=ext_gcd(a,b)
    if gcd!=1:
        raise Exception("bad")
    else:
        return x%b

def finde(n):
    while True:
        num=random.randint(2,n-1)
        if ext_gcd(num,n)[0]==1:
            return num
        
    

def generate_keys(bits):
    p=generate_prime(bits)
    q=generate_prime(bits)
    while p==q:
        q=generate_prime(bits)
    n=p*q
    phi=(p-1)*(q-1)
    e=finde(phi)
    d=mod_inv(e,phi)
    public=(e,n)
    private=(d,n)
    return public,private

def encrypt(message,keys):
    e=keys[0]
    n=keys[1]
    
    ciphertext=[pow(ord(x),e,n) for x in message]
    return ciphertext

def decrypt(cipher,keys):
    d=keys[0]
    n=keys[1]
    
    message=''.join([chr(pow(x,d,n)) for x in cipher])
    return message
if __name__=="__main__":
    bits=1024
    
    public_key,private_key=generate_keys(bits)
    
    message=input("enter message")
    ciphertext=encrypt(message,public_key)
    print("the cipher is " + str(ciphertext))
    
    dec_message=decrypt(ciphertext,private_key)
    print("the decry mess is " + str(dec_message))
    # print(p)
    
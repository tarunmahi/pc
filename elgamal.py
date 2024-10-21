import random

def miller(n,k=5):
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
        if x==1 or x==n-1:
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
        num=random.getrandbits(bits)
        if miller(num):
            return num

def test(g,num):
    n=num-1
    factors=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            factors.add(i)
            n//=i
    if n>1:
        factors.add(n)
    for x in factors:
        if pow(g,(num-1)//x,num)==1:
            return False
    return True
    

def gen(p):
    while True:
        for i in range(2,p):
            if test(i,p):
                return i

def gen_b():
    p=generate_prime(32)
    g=gen(p)
    b=random.randint(2,p)
    B=pow(g,b,p)
    return p,g,B,b

def gen_a(p,g,B):
    message=input("enter secret message")
    code=[ord(x) for x in message]
    a=random.randint(2,p)
    c1=pow(g,a,p)
    s=pow(B,a,p)
    c2=[(char*s)%p for char in code]
    return c1,c2

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
def modinverse(a,b):
    gcd,x,y=ext_gcd(a,b)
    return x%b     
    
def bob_dec(c1,c2,p,g,B,b):
    shared_sec=pow(c1,b,p)
    s1=modinverse(shared_sec,p)
    decrptedmess=''.join([chr((char*s1)%p)for char in c2])
    return decrptedmess
    

if __name__=="__main__":
    shared_bob=gen_b()
    p=shared_bob[0]
    g=shared_bob[1]
    B=shared_bob[2]
    print(f"the values shared by bob are P : {p}, g : {g}, B : {B}")
    shared_alice=gen_a(p,g,B)
    c1=shared_alice[0]
    c2=shared_alice[1]
    b=shared_bob[3]
    print(f"the values shared by Alice are c1 : {c1}, c2 : {c2}")
    bob=bob_dec(c1,c2,p,g,B,b)
    print(f"{bob}")
    
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
 
def test(num,p):
    factors=set()
    n=p-1
    for i in range(2,int(num**0.5)+1):
        if n%i==0:
            factors.add(i)
            n//=i
    if n>1:
        factors.add(n)
    for x in factors:
        if pow(num,p-1//x,p)==1:
            return False
    return True
            
     
 
 
def gen_gen(p):
    while True:
        for i in range(2,p):
            if test(i,p):
                return i   
    
    
def generate_prme(num):
    while True:
        number=random.getrandbits(num)
        if millertest(number):
            return number    

if __name__=="__main__":
    p=generate_prme(128)
    g=gen_gen(p)
    print(f"P: {p} and g: {g} \n")
    key_a=random.randint(2,p)
    key_b=random.randint(2,p)
    while key_a==key_b:
        key_b=random.randint(2,p)
    X_a=pow(g,key_a,p)
    Y_b=pow(g,key_b,p)
    print(f"secrest shared by alice is {X_a} \n")
    print(f"secrest shared by bob is {Y_b}")
    
    dec_b=pow(X_a,key_b,p)
    dec_a=pow(Y_b,key_a,p)
    
    print(f" decrypted by alice is {dec_a} and that of bob {dec_b}")
    
    
   
    
    
 
def prime_check(x):
    if x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        if i==x-1:
            return True

def next_prime(t):
    if t==1:
        return 2
    if prime_check(t):
        return t
    else:
        i=1
        while True:
            if prime_check(t+i):
                return t+i
            i+=1

def phi(p,q):
    return (p-1)*(q-1)

def factors(x):
    l=[]
    for i in range(2,x+1):
        if x%i==0:
            l.append(i)
    return l


def coprime(a,b):
    a=factors(a)
    b=factors(b)
    for i in a:
        if i in b:
            return False
    return True


def choose_e(N,ph):
    for i in range(2,ph):
        if coprime(i,N) and coprime(i,ph):
            return i

def choose_d(e,ph):
    i=1
    a=0
    while True:
        t=e*i
        if t%ph == 1:
            if a==2:
                return i
            else:
                a+=1
        i+=1
    

def keys(message,encrypt):
    
    total=0
    for i in message:
       total+=ord(i)
    q=next_prime(total)
    p=2
    N=p*q
    ph=phi(p,q) 

    e=choose_e(N,ph)
    if encrypt: 
        lock=(e,N)
        return lock
    
    else:
        d=choose_d(e,ph)
        key=(d,N)
        return key


def rsa(message,a,b,encrypt):
    l=[]
    t=''
    for i in message:
        l.append(i)
    for i in range(0,len(l)):
        l[i]=ord(l[i])
    
    for i in range(0,len(l)):
        l[i]=(l[i]**a)%b
    
    for i in range(0,len(l)):
        l[i]=chr(l[i])
    if encrypt:
        return l
    else:
        for i in l:
            t+=str(i)
        return t
    
        
"""x=input("Enter your message: ")
t=x
x=rsa(x,keys(t,True)[0],keys(t,True)[1],True)
print(x)
x=rsa(x,keys(t,False)[0],keys(t,False)[1],False)
print(x)"""
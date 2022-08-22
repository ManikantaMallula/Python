def isprime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

def twinprime(s,e):
    for i in range(s,e):
        j=i+2
        if isprime(i) and isprime(j):
            print(i,j," are prime numbers")
twinprime(1,50)





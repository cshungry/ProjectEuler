# link of problem  https://projecteuler.net/problem=25

def fibo():
    l=[0,1,1] 
    i=3
    while True:
        l.append(l[i-1]+l[i-2])
        if len(str(l[i]))==1000:
            return i
        i+=1
print(fibo())

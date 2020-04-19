def prime(n):
    i=2
    while i**2<=n:
        if n%i==0:
            return False
        i+=1
    return True

tc=int(input())
for _ in range(tc):
    n=int(input())
    summ=0
    while n>=2:
        if prime(n)==True:
            summ+=n
        n-=1
    print(summ)

def fact(n):
    f=1
    while n>1:
        f*=n
        n-=1
    s=str(f)
    summ=0
    for i in s:
        summ+=int(i)
    return summ
tc=int(input()) # number test case take 1 
for _ in range(tc):
    n=int(input())
    print(fact(n))

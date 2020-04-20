def fact(n):
    f=1
    while n>0:
        f*=n
        n-=1
    return f
def curious(n):
    temp=n
    summ=0
    while temp>0:
        rem=temp%10
        summ+=fact(rem)
        temp//=10
    if summ==n:
        return True
    return False

s=0
for i in range(3,45000):
    if curious(i)==True:
        s+=i
print(s)

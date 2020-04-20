def fifthPow(n):
    temp,summ=n,0
    while temp>0:
        rem=temp%10
        summ+=rem**5
        temp//=10
    if summ==n:
        return True
    return False
s=0
for i in range(2,200000):
    if fifthPow(i)==True:
        s+=i
print(s)

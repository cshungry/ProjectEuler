l=[]    #list to track the calculated amicable number
def comp(n,summ):
    if n==divisor(summ): 
        return True
    return False

def divisor(n):
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    return summ 
for n in range(2,10001):
    if n in l:  # if we already amicable number i.e summ
        continue
    summ=divisor(n)
    if summ==n: # number and summ of divisor should not be equal
        continue
    if comp(n,summ):
        l.append(n)
        l.append(summ)

print(sum(l))
    

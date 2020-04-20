import math
def primefact(n):   # function for prime factor
    maxi=2          # to store largest prime factor
    while n%2==0:
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            n//=i
            maxi=i  # prime factor(i) always greater than maxi 

    if n>maxi:  # if number itself is prime number
        maxi=n
    return maxi

tc=int(input()) #for multiple test case or put 1
for _ in range(tc):
    n=int(input())

    print(primefact(n))

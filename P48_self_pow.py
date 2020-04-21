# link https://projecteuler.net/problem=48
summ=0
for i in range(1,1001):
    summ+=i**i

s=str(summ)
print(s[-10:]) #last 10 digit of summ

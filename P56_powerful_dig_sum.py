def digsum(a):
    summ=0
    for i in a:
        summ+=int(i)
    return summ

maxi=0
for i in range(1,101):
    for j in range(1,101):
        summ=digsum(str(i**j))
        if summ>maxi:
            maxi=summ
print(maxi)

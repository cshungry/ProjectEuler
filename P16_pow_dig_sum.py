tc=int(input())
for _ in range(tc):
    n=int(input())
    s=str(2**n)
    summ=0
    for i in s:
        summ+=int(i)

    print(summ)

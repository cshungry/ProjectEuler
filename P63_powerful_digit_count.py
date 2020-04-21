cnt=0
for n in range(1,25):   # 25^25 is quite large number it will cover all cases
    for a in range(1,25):
        if len(str(a**n))==n:
            cnt+=1
print(cnt)

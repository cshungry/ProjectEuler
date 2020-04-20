# link https://projecteuler.net/problem=29
s=set()
for a in range(2,101):
    for b in range(2,101):
        s.add(a**b) # if element are not present then add in set
                    # therefore no duplicate value exist in set
print(len(s))  # all element in set is distinct

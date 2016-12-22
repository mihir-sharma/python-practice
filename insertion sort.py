insort = [85, 56, 45, 77, 62, 21, 54]

for j in range(1,len(insort)):
    key = insort[j]
    i=j-1
    while j>=0 and insort[i]> key and i>=0 and j>=0:
        key = insort[j]
        temp = insort[i+1]
        insort[i+1] = insort[i]
        insort[i] = temp
        i=i-1
        j=j-1
print(insort)
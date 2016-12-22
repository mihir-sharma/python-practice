def mergesort(somelist):
    if len(somelist) > 1:
        mid = len(somelist)//2
        left = somelist[:mid]
        right = somelist[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                somelist[k] = left[i]
                i=i+1
            else :
                somelist[k] = right[j]
                j=j+1
            k=k+1

        while i<len(left):
            somelist[k] = left[i]
            i=i+1
            k=k+1

        while j<len(right):
            somelist[k] = right[j]
            j=j+1
            k=k+1

mergetest = [62,31,102,12,80,26,50,53,19]
mergesort(mergetest)
print(mergetest)
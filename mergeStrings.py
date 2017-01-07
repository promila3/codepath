def  mergeStrings(a, b):
    lena = len(a)
    lenb = len(b)
    result = ""
    i, j = 0, 0
    while (i < lena ) and (j < lenb):
        result += a[i] + b[j]
        i +=1
        j +=1
    print i, j
    print result
    while (i <lena) :
        result += a[i]
        i +=1
    while (j <lenb):
        result += b[j]
        j +=1
    return result

a = "ab"
b = "zsd"

print mergeStrings(a,b)

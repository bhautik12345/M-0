#largest element
l = [3,4,2,1,0]
def largest(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        break
    return l[-1]

print(largest(l))

#smallest element

def smallest(obj):
    n = len(obj)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n,1):
            if obj[j] < obj[min_index]:
                min_index = j
        if min_index != i:
            obj[i], obj[min_index] = obj[min_index], obj[i]
        break
    return obj[0]

# print(smallest(l))


    


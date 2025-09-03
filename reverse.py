l = [1,"bhautik",True,99.99,5]
text = "Bhautik Vadaliya"

def reverse(obj):
    for i in range(len(obj)-1,-1,-1):
        print(obj[i], end=" ")
    else:
        print("\nComplete!")

reverse(text)





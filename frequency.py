def freq(obj):
    if isinstance(obj, str):
        obj = obj.lower()
        
    d = {}
    for ele in obj:
        d[ele] = d.get(ele, 0) + 1
    print(d)
obj = [1,2,"bhautik",True,1,3,3,"bhautik",True,0,False]
obj1 = "Bhautik Vadaliya"
freq(obj1)

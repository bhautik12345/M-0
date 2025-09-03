def duplicates(l):
    # new_list = list(set(l))

    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)

    print(new_list)

l = [1,2,"bv",2,True,True,0]
duplicates(l)

def merge_list(list1, list2):
    merged_list = []
    pt1 = 0
    pt2 = 0

    while (pt1 < len(list1) and pt2 < len(list2)):
        if list1[pt1] < list2[pt2]:
            merged_list.append(list1[pt1])
            pt1 += 1
        else:
            merged_list.append(list2[pt2])
            pt2 +=1

    while pt1 < len(list1):
        merged_list.append(list1[pt1])
        pt1 += 1

    while pt2 < len(list2):
        merged_list.append(list2[pt2])
        pt2 += 1

    return merged_list

l1 = [1,3,5,7,9,10]
l2 = [2,4,6,8]

print(merge_list(l1, l2))
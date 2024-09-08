# write a program in python to merge 2 sorted lists till length n
def merge_sorted_lists(list1, list2, n):
    i, j = 0, 0
    merged_list = []
    while len(merged_list) < n and i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while len(merged_list) < n and i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while len(merged_list) < n and j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return (merged_list)

list1 = [4,7,9,10]
list2 = [1,5,10,20]
n = 5
merged_list = merge_sorted_lists(list1, list2, n)
print(merged_list)


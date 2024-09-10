# Find top K most frequent items in a list
def find_frequent(items, k):
    item_dict = {}
    for item in items:
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    print(item_dict)
    sorted_dict = sorted(item_dict, key=item_dict.get, reverse=True)
    print(sorted_dict[:k])

items =  [4, 1, 1, 2, 2, 3, 1, 4, 4, 4]
k = 2
answer = find_frequent(items, k)
print(answer)

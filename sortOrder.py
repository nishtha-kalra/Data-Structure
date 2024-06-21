'''
Sort arbitary inputs in given order
input: abcab
order: bca
ouput: bbcaa
'''

def sortOrder(inout, order):
    dictionary = {}
    for i in input:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    output = []
    for o in order:
        if o in dictionary:
            output.append(o*dictionary[o])
    return(''.join(output))

input = 'abcab'
order = 'bca'
output = sortOrder(input, order)
print('output:', output)

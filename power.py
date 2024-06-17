def power(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * power(n, p-1)

def power1(n, p):
    product = 1
    for _ in range(p):
        product = product * n
    return product

ans = power(3,3)
print(ans)
ans1 = power1(3,3)
print(ans1)

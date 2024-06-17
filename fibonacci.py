# recursive way
def fib1(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
    
# Memoized Recursive     
def fib2(n, mem={}):
    if n in mem:
        return mem[n]
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        mem[n] = fib2(n-1, mem) + fib2(n-2, mem)
        return mem[n]

# iterative way
def fib3(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for i in range(n-1):
        c = a + b 
        a = b 
        b = c
    return c

answer1 = fib1(10)
print('recusrsive way:', answer1)
answer2 = fib2(10)
print('memoization way:', answer2)
answer3 = fib3(10)
print('iterative way:', answer3)
    

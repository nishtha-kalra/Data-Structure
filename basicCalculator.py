def calculate(s: str):
    stack = []
    num = 0
    sign = '+'
    final_sum = 0
    i = 0
    while i < len(s):
        n = s[i]
        print('n:', n)
        if n.isdigit():
            num = num * 10 + int(n)
            print("num:", num)
        if n in ['+', '-', '*', '/'] or i == len(s) - 1:
            print('sign:', n)
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                last_n = stack.pop()
                stack.append(last_n * num)
            if sign == '/':
                last_n = stack.pop()
                stack.append(last_n / num)  
            num = 0
            sign = n
            print('stack:', stack)
        i += 1
    final_sum = sum(stack)
    return(final_sum)

s = '18-3*12+6'
output = calculate(s)
print(output)

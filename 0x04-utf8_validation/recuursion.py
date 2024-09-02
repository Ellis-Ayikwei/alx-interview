#!/usr/bin/env python3

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return [0,1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list 

# if __name__ == "__main__":
#     print(fibonacci(200))
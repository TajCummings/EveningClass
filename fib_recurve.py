def fib(x):
    if(x <= 2):
        return 1
    else:
        r = fib(x-1) + fib(x-2)
        return r


def fib2(x):
    if x <= 2:
        return 1
    
    if x in memo:
        return memo[x]
    else:
        r = fib2(x-1) + fib2(x-2)
        memo[x] = r
        return r


memo = {}
print(fib(7))
print(fib2(7))



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


def grid_trav(m,n):
    key = (str(m) + ',' + str(n))

    if(key in memo):
        return memo[key]
    if(m == 1 and n == 1):
        return 1
    if(m == 0 or n == 0):
        return 0

    memo[key] = grid_trav(m - 1, n) + grid_trav(m, n - 1)
    return memo[key]

#print(grid_trav(1, 1))
print(grid_trav(2, 3))
print(memo)
#print(grid_trav(3, 2))
#print(grid_trav(18, 18))

#print(fib2(40))



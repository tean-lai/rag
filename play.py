import cProfile

def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

cProfile.run("x = 10")

print(x)
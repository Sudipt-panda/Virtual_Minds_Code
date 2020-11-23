fib = {0: 0, 1: 1}
#############
def nth_fib(n):
    if not n in fib:
        fib[n] = nth_fib(n - 1) + nth_fib(n - 2)
    return fib[n]
###############
def main():
    i = 0
    while (True):
        if (len(str(nth_fib(i))) == 1000):
            print(i)
            break
        i = i + 1
###############
main()

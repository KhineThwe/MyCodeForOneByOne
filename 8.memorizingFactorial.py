#memorizing
def memorize(fibo):
    cache = dict()#akone မှတ်လို့ရအောင်
    def inner(n):
        if n not in cache:
           cache[n] = fibo(n)
        return cache[n]
    return inner

@memorize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n<2 else n*fact(n-1)
print(fact(5))
print(fact(6))
print(fact(10))

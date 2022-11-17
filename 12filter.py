#zip function
alphabet = ['a','b','c','d','e','f','i','o','u','j','k']

def vowel_filter(alpha):
    vowel =['a','e','i','o','u']
    if(alpha in vowel):
        return True
    else:
        return False
#filter function takes two argument function and iterable 1 ku
results = filter(vowel_filter,alphabet)
print(results)
for i in results:
    print(i)

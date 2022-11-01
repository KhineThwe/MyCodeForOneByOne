#function passing through a function
#function ထဲမှာ function ka parameter အနေနဲ့ဖြတ်သွားမယ်

def square(a):#parameter a
    return a**2

def cube(b):
    return b**3

def funTofun(fun,n):#funname ,parameter number 1 ku ku
    return fun(n)

a = funTofun(cube,3)#cube 3 fun return pyan lr mal
print('Calling cube function',a)

b = funTofun(square,4)
print('Calling square function',b)

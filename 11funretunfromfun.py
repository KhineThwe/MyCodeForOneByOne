#returning function from a function
#function keyword ka def
def square(a):#parameter a
    return a**2

def cube(b):
    return b**3

#fun call
def num(number):
    if number == 1:
        return square #fun return 
    else:
        return cube#fun return 

sq = num(1)#square function ka ll memory address 1 ku shi tal ae address ko assign lote tr
#sq ကို မြင်တာနဲ့ square ko tan myin ya mhar 
print(sq(10))

cu = num(2)
print(cu(3))

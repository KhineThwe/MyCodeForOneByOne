#function ------> reusable 
#return keyword

def greet(name):#1 parameter
   print(f'Hello,{name}')

greet('Khine')


#parameter 2 
# def area(width,height):
#     print(width*height)
    
# area(12,20)


#return keyword
def area(width,height):
    return (width*height)
    
result = area(12,20)
print(result)

#default value or parameter
def greet1(name="Khine"):
    print(f"Hello{name}'")
greet1()



def repeat(text,times):
    for i in range(times):
        print(text)

repeat("KO KO",3)

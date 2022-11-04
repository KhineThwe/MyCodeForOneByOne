#lambda expression or anonymous function
#no def keyword and no function name
#function object တစ်ခု return ပြန်ပေးတယ်
#one parameter
# x = lambda y:y*2
# #function call ka x loe pl call loe ya dal
# print(x(3))
# print(x)

#two parameter with keyword argument
# x = lambda y,z=10:y*z
# print(x(2,2))

#with arbitary argument
x = lambda x,*args,y,**kwargs:(x,args,y,kwargs)
print(x(10,'a','b',y=10,i=10,j=20,k=30))

#return whole tuple
#kwargs ka dictionary style




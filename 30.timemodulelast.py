#Time Module
#time.py loe ma yay nae 
#node.js mhar so package python mhar so yin Module
#The perf_counter() function always
#returns the float value of time in seconds.
#repeat ==> frequency count

#You can use *args and **kwargs as arguments of a function when you are unsure about the number of arguments to pass in the functions.
def myFun(fn,*args,rep=1,**kwargs):
    start = time.perf_counter()#start time
    #it will return time
    for i in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()#loop pat pi thar
    avgTime =(end-start)/rep
    fn(avgTime)
myFun(print,1,2,3,sep='-',end='***\n',rep=5)



class Price:
    def payment(self,*args):#arbitrary argument
        data = 0
        count = 0
        for i in args:
            count+=1
            data = data+i
        print('There are {0} parameter passed'.format(count))
        return data


obj = Price()
print(obj.payment(10,5))
print(obj.payment(2,2,2,2,2,2,2,2))
# print(obj.payment('aung','aung'))#TypeError

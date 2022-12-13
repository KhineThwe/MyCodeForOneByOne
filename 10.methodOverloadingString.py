#method overloading string
class Price:
    def payment(self,dataType,*args):#arbitrary argument
        if dataType == "int":
            data = 0
            count = 0
            for i in args:
                count += 1
                data = data + i
            print('There are {0} parameter passed'.format(count))
            return data
        elif dataType == "str":
            data = ''
            count = 0
            for i in args:
                count += 1
                data = data + i
            print('There are {0} parameter passed'.format(count))
            return data
obj = Price()
print(obj.payment('int',10,5))
print(obj.payment('int',2,2,2,2,2,2,2,2))
print(obj.payment('str','aung','aung'))

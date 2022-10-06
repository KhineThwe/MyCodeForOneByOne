import random
class lottery:
    def __init__(self,name,age):#special method #constructor
        print("Welcome from Our Lottery Game!!!")
        self.name = name
        self.age = age
    
    def generate_no(self):
        random_no = random.randint(0,99)
        return random_no
    
    
if __name__ == "__main__":    
    lt = lottery("Khine",24)
    lottery_no = lt.generate_no()
    # lottery_no = 55
    print(lottery_no)
    
    user_amount = int(input("Please enter your amount: "))
    
    option = input("Press 1 to play game:Press 2 to quit: ")
    while option=='1': 
        play_amount = int(input("Please enter your play amount: "))
        if user_amount < play_amount:
            print("Insufficient Balance!!Please sufficient balance again!")
            user_amount = int(input("Please enter your amount: "))            
        else:
            play_no = int(input("Please enter your play no: "))
            if play_no == lottery_no:
               print("Hit")
               user_amount+=play_amount*5   
            else:
               print("Lose")   
               user_amount-=play_amount     
            print("Your current cash: ",user_amount)
            if user_amount == 0:
                exit(0)
            option = input("Press 1 to play game:Press 2 to quit: ")
            
        
    
    
    

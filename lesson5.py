import math
secretNumber = 0
computerGuess = 50
low = 1
high = 100
guessCorrect = False
higher = False
invalid = True

def findMedian():    
    global low, high, computerGuess
    if computerGuess  == 2:
        return 1
    else:
       return math.ceil((int(low)+int(high)) / 2)

def changeRange(higher):
    global low, high, computerGuess
    
    if higher == True:
        low=computerGuess
    elif higher == False:
        high = computerGuess
        
secretNumber = int(input("Pick a number 1-100: "))
        
if int(secretNumber) < 1 or int(secretNumber) > 100:
        print("Invalid Number")

else:
    while guessCorrect == False:
        print(computerGuess)
        answer = input("Is this number correct? yes or no: ")
        
       
        if answer == "yes":
            guessCorrect = True
       
            print("Haha I guessed your number. It was TOO EASY HAHAHA.")

        elif answer == "no":
            guessCorrect = False
            higher = input("is it higher or lower: ")
           
            if higher == "higher":
                higher = True
            
            elif higher == "lower":
                higher = False   
            
            else:
                higher = input("is it higher or lower: ")
                
        changeRange(higher)
        
        computerGuess = findMedian()
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




             
            
            
            


        
    
        
        




    
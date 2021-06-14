#Programming Principles(1)/Course Work 2019

#Part 1-Student Version

#Defining Variables

pas=0
fail=0
defer=0
total=0

while True:
        try:
            n = int(input("Enter your student ID: "))
        except ValueError:
            print("integer required")                  # Integer Error Checking
            
#Creating Variables            

        def a():                                          
            try:
                pas= int(input("Enter the pass mark: "))
            except ValueError:
                
                print("integer required")              # Integer Error Checking
                return a()
        
            if (pas !=0)and(pas !=20)and(pas !=40)and(pas !=60)and(pas !=80)and(pas !=100)and(pas !=120):

                print("Range Error")                   # Range Error Checking
                return a()                                     
            else:
                    passes=pas
                    return pas


            

        def b():                                        
            try:
                defer= int(input("Enter the defer mark: "))
            except ValueError:
                   
                print("interger required")              # Integer Error Checking
                return b()
            if (defer !=0)and(defer !=20)and(defer !=40)and(defer !=60)and(defer !=80)and(defer !=100)and(defer !=120):
               
               print("Range Error")                     # Range Error Checking
               return b()
            else:
                    defers=defer
                    return defers 
        def c():                                        
            try:
               
                fail= int (input("Enter the fail mark: "))
            except ValueError:
                 print("interger required")             # Integer Error Checking
                 return c()
            if (fail !=0)and(fail !=20)and(fail !=40)and(fail !=60)and(fail !=80)and(fail !=100)and(fail !=120):

                print("Range Error")                    # Range Error Checking
                return c()
            else:
                    fails=fail
                    return fail
                   
           
        passes=(a())
        defers=(b())
        fails=(c())
        total=passes+fails+defers
        
        if total!=120:
               print("Total incorrect")                  # Total Checking
               break
                
        
    #logical Variables
      
        if passes==120:
                print("Progress \n")
                break
        elif passes==100:
                print("Progress-module trailer \n")
                break
        elif (fails>= 80) and(fails<= 120):
                print("Exclude \n")
                break
        else:
                print("Do not progress-module retriever \n")
                break
        
                    
   
      



 

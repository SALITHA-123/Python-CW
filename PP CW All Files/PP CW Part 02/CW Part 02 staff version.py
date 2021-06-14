#Programming Principles(1)/Course Work 2019

#Part 2-Staff Version

# Defining Variables

pas=0
fail=0
defer=0
total=0
pcount=0
tcount=0
retcount=0
excount=0
total_outcome=0


option=input("Press q to quit or  Press any other key to continue:")
while option!='q':
        try:
            n = int(input("Enter your student ID: "))
        except ValueError:
            print("interger required")                    # Integer Error Checking
            
#Creating Variables            

        def a():    
            try:
                pas= int(input("Enter the pass mark: "))
            except ValueError:
                
                print("interger required")                # Integer Error Checking
                return a()
        
            if (pas !=0)and(pas !=20)and(pas !=40)and(pas !=60)and(pas !=80)and(pas !=100)and(pas !=120):

                print("Range Error")                      # Range Error Checking
                return a()
            else:
                    passes=pas
                    return pas


            

        def b():
            try:
                defer= int(input("Enter the defer mark: "))
            except ValueError:
                   
                print("interger required")                # Integer Error Checking
                return b()
            if (defer !=0)and(defer !=20)and(defer !=40)and(defer !=60)and(defer !=80)and(defer !=100)and(defer !=120):
               
               print("Range Error")                       # Range Error Checking
               return b()
            else:
                    defers=defer
                    return defers 
        def c():
            try:
               
                fail= int (input("Enter the fail mark: "))
            except ValueError:
                 print("interger required")               # Integer Error Checking
                 return c()
            if (fail !=0)and(fail !=20)and(fail !=40)and(fail !=60)and(fail !=80)and(fail !=100)and(fail !=120):

                print("Range Error")                      # Range Error Checking          
                return c()
            else:
                    fails=fail
                    return fail
                   
           
        passes=(a())
        defers=(b())
        fails=(c())
        total=passes+fails+defers
        
        if total!=120:
               print("Total incorrect")                  #Total Cheaking
               a()
               b()
               c()
                
        
    #logical Variables
      
        if passes==120:
                print("Progress \n")
                pcount+=1

        elif passes==100:
                print("Progress-module trailer \n")
                tcount+=1

        elif (fails>= 80) and(fails<= 120):
                print("Exclude \n")
                excount+=1
        else:
                print("Do not progress-module retriever \n")
                retcount+=1
        option=input("Enter q to quit any other key to continue:")
                
                    
total_outcome=pcount+tcount+excount+retcount


print("progress ",pcount,":",end=' ')
for i in range(0,pcount):
    print('*',end='')
print('\n')

print("trailer ",tcount,":",end=' ')
for i in range(0,tcount):
    print('*',end='')
print('\n')

print("retriever ",retcount,":",end=' ')
for i in range(0,retcount):
    print('*',end='')
print('\n')

print("exclude ",excount,":",end=' ')
for i in range(0,excount):
    print('*',end='')
print('\n')
   
          
print(total_outcome,"Outcomes in total")
      

 

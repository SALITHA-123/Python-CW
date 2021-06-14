pas=0
#Programming Principles(1)/Course Work 2019

#Part 1-Student Version

#Creating Variables

fail=0
defer=0
total=0
pcount=0
tcount=0
retcount=0
excount=0
total_outcome=0

#Creating the List

marklist=[[120,0,0],[100,20,0],[80,40,0],[60,60,0],[40,40,40],[20,80,20],[0,0,120],[0,60,60],[40,80,0],[100,0,20]]
count = len(marklist)

for x in range (0,count):
   sublist= marklist[x]
   
   pas= sublist[0]
   if(pas !=0)and(pas !=20)and(pas !=40)and(pas !=60)and(pas !=80)and(pas !=100)and(pas !=120):
      print("Range Error",'/n')
      break

   defer= sublist[1]
   if (defer !=0)and(defer !=20)and(defer !=40)and(defer !=60)and(defer !=80)and(defer !=100)and(defer !=120):
      print("Range Error",'/n')
      break
      
   fail= sublist[2]
   if (fail !=0)and(fail !=20)and(fail !=40)and(fail !=60)and(fail !=80)and(fail !=100)and(fail !=120):
      print("Range Error",'/n')
      break
   
   
   total=pas+fail+defer
   
   if total>120:
      print("Total Error")
      break

   if pas==120:
      
      pcount+=1
      
   elif int(pas)==100:
      
      tcount+=1
      
   elif (fail>= 80) and(fail<= 120):
      
      excount+=1
   else:
      
      retcount+=1
      
      

print("progress ",pcount,":",end=' ')
for i in range(0,pcount):
   print('*',end='')
print('\n') 


print("trailer ",tcount,":",end=' ')
for i in range(0,tcount):
   print('*',end=' ')
print('\n')   

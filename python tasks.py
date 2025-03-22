#factorial

# n = 4
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

# #GCD  greatest common divisor

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# a = int(input("Enter value for a:100 "))
# b = int(input("Enter value for b: 50"))

# GCD = gcd(a, b)
# print("The GCD of the given two numbers is:", GCD)
# print (GCD)


#amstrong number

# { no=153
#  arm=0
#  while (no>0):
#  rem =153 %10
#  arm = arm+(15*15*15)
#  no =15/10
#  }

# num = int (input("153")
# sum=0
# temp=num 
# while temp >0:
#     digit =temp %10 

#find leap year or not 

# year = int(input("enter the year:"))

# if (year %4 ==0 and year % 100 !=0) or year %400 ==0:
#     print(year,"is leap year")
# else:
#     print(year,"is not leap year")


# palindrome is a word or sentence that remains same forward and also backward
#[::-1]   is palindrome -1 used for reverse

# word = input ("enter your word to find palindrome or not :")
# rev = (word[::-1])
# if rev== word :
#     print ("the word is palindrome.")
# else:
#     print ("the word is not palindrome.")

# fibonacci series   by adding before two values we will get the next value
# count = int(input("enter the time fibonacci series needed"))
# num 1 =0
# num 2 =1 
# iter  = 0 

# if count <=0:
#     print ('the count has to be greater than 0:')
# else :
#     print('the fibonacci series:', end ="")
#     print ('the fibonacci series:',end =" ")
#     while (iter <count):
#         print (num1)
#         nextnum = num1+num2 
#         num1 = num2 
#         num2 = nextnum
#         iter = iter+1  


#  removing duplicate values from the list
# l1= (1,2,3,4,5,1,2,7,9)
# print("this is my list:",l1)
# print ("a list with out removing duplicate values:",list(set(l1)))
# set(l1)

# l2=[1,2,3,4]
# l3=[1,2,6,7]



# multithreading is just performing a task

# from threading import*
# from time import*
# class java (thread):
#     def run(self):
#         for i in range(3):
#             print("learning java")
#             sleep(3)
# class python (thread):
#     def run (self):
#         for i in range(5):
#             print (learning python)
#             sleep(9)
# def main ():
#     print("placement started")
#     j=java()
#     p=python()
#     p.start()
#     j.start()
#     p.join()
#     p.join()
#     print ("placement end")
# main()



# #multi threading  
# from threading import Thread
# from time import sleep
 
# class Java(Thread):  # Class names should typically start with an uppercase letter
#     def run(self):
#         for i in range(3):
#             print("Learning Java")  # Fixed string formatting
#             sleep(3)

# class Python(Thread):  # Class names should typically start with an uppercase letter
#     def run(self):
#         for i in range(5):
#             print("Learning Python")  # Fixed string formatting
#             sleep(9)

# def main():
#     print("Placement started")
#     j = Java()  # Instantiate the Java thread
#     p = Python()  # Instantiate the Python thread
#     p.start()  # Start the Python thread
#     j.start()  # Start the Java thread
#     p.join()  # Wait for the Python thread to finish
#     j.join()  # Wait for the Java thread to finish
#     print("Placement ended")

# main()


# f=open ("sugan s.txt","r")
# print (f.read())

f = open("fruits.txt")  # Opens the file in read mode
content=f.read()
print(content)




# f=open ("python.txt","w")
# f.write ("transflow is used for ml")
# f.close()






















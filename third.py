#for i in range(5):
  #  print(i)
##for i in range(1,10,2):
##   print(i)
##fruits={"apple","mango","banana"}
##for fruit in fruits:
##    print(fruit)
##def both(a,b):
   ## return a+b,a-b,a*b,a//b,a%b
##print(both(10,5))
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
        return result
    
    
    print(factorial(5))
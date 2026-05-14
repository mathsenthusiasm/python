n=int(input("enter any number:"))
c=n
rev=0
while n!=0 :
        r=n%10
        rev=rev*10+r
        n=n//10
if(c==rev):
    print("palindrome")
else:
    print("not palindrome")

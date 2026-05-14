def is_in_range(num,low,high):
    return low<=num<=high
num=int(input("enter any number:"))
low=int(input("enter any number:"))
high=int(input("enter any number:"))
if(is_in_range(num,low,high)):
        print(f"{num} is in the range={low},{high}")
else:
        print(f"{num} is not in the range={low},{high}")
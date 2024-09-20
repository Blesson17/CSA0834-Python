num=int(input("enter the number:"))
if num==1:
    print("is not a prime number")
if num>1:
    for n in range(2,num):
        if num%2:
            print("is a prime number")

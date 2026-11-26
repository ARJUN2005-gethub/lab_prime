n = int(input("Enter the number : "))
if(n<=2):
    print("Not a Prime Number")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not Prime Number")
            break
    else:
            print("Prime number")

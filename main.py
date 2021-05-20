a = int (input ("Enter an integer value to start odd/even number:"))
b = int (input ("Enter an integer value to end odd/even number:"))

if a > b:
    print("Incorrect Inputs")
else:
    num = a
    if a%2==0:
        a+=1

    #Print Odd Numbers
    print("Printing ODD Numbers ....")
    while a <=b :
        print(a)
        a+=2

    a = num
    if a%2!=0:
        a+=1

    print("Printing Even Numbers ....")
    # Print Even Numbers
    while a <=b :
        print(a)
        a+=2


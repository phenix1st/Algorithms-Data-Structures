def PrintPrimes(number) :
    x=1
    print(f"the prime numbers from 1 to {number} are : ")
    two=True
    alltwo=True

    while x < number :
        if number %2==0 and two==True :
            two = False
            print(2)
        if number % x == 0 and x % 2 !=0 :
            print(x)
        x+=2
    
    print(number)
hell=input("enter a number : ")
PrintPrimes(int(hell))
        
            
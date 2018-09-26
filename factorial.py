def factorial(n):
    f = 1
    for i in range (n,0,-1):
        f = f*n
        n= n-1

    print(f)    
num = input("enter your number")
factorial (int(num))        

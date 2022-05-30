try:
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b 
#a=  N and b=0
    print(c)    
    
#other code:    
except ZeroDivisionError:
    print("Try to division by 0 ")

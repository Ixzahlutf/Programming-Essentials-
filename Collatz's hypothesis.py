c0 = int(input("Enter a Number  :"))
steps = 0
while True :    
    if c0!= 1 :
        if c0 % 2 == 0 :
            c0 = int(c0/2)
            print(c0)
        else :
             c0 = 3*c0+1
             print(c0)
        steps +=1
    else :
        break
    
print("Steps",steps)

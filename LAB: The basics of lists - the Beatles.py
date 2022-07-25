# step 1
beatles =[]
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input("enter another singer name    :"))
print("Step 3:", beatles)

# step 4
for i in range(int(input("How much you want to delete?  :"))):
    number = int(input("Which list?(must number):"))
    list_number = number-1
    del beatles[list_number]
    print(beatles)
    
print("Step 4:", beatles)

# step 5
beatles.insert(0,'Ringo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

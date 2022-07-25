blocks = int(input("Enter the number of blocks: "))
height = 0
while True :
    for i in range(1,blocks):
      if blocks != 0 and blocks>i-1:
        blocks = blocks - i
        height += 1
    break
print("The height of the pyramid:", height)

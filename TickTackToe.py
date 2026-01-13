import random
#hello!
topline = [" 1", "|", "2", "|", "3"]
line = ["---", "---", "---"]
midline = [" 4", "|", "5", "|", "6"]
bottomline = [" 7", "|", "8", "|", "9"]
print("Welcome to Tik-Tac-Toe")
print()

print(topline[0],topline[1],topline[2],topline[3], topline[4])
print(line[0],line[1],line[2])
print(midline[0],midline[1],midline[2],midline[3], midline[4])
print(line[0],line[1],line[2])
print(bottomline[0],bottomline[1],bottomline[2],bottomline[3], bottomline[4])

X =" X"
cpu = random.choice([1,2,3,4,5,6,7,8,9])
print()
player = int(input("Were would you like to go (1-9): "))

if player == 1:
    topline[0] = X
    print(topline[0],topline[1],topline[2],topline[3], topline[4])
    print(line[0],line[1],line[2])
    print(midline[0],midline[1],midline[2],midline[3], midline[4])
    print(line[0],line[1],line[2])
    print(bottomline[0],bottomline[1],bottomline[2],bottomline[3], bottomline[4])
    
    

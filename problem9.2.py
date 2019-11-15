h = 0

while h == 0:
    u = (input("\ninput half of the pyramids height, must be between 1 and 8\n")

    try:
        n = int(u)
    except ValueError:
        print("A number!")

        
    if n > 8 or n < 1:
        print("Between 1 and 8!")
    else:
        h = 1
    

r = n * 2
for i in range(r):
  for j in range(i+1):
    print("#", end="")
  print("")
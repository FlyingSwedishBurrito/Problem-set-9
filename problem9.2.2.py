h = 0

while h == 0:
    n = int(input("Height:"))

    if n > 8 or n < 1:
        print("Between 1 and 8!")
    else:
        h = 1

for i in range(n):
  for j in range(i+1):
    print("#", end="")
  print("")
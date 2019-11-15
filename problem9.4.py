n = int(input("\ninput number of #'s you want in the base of pyramid\n"))



if n % 2 == 0:
    w = 2
    r = int(n / 2)
else:
    w = 1
    r = int((n + 1) / 2)
    
s = r - 1

for i in range(r):
    for j in range(n):
        if j < s:
            print(" ",end="")
        elif j < w + s:
            print("#", end="")
        
    w += 2
    s -= 1
    print("")
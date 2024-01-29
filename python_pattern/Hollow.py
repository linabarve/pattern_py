"""n = 6  
k = 0
for i in range(n):
    if i == 1:
    	print('*')
    if i == n and i == n:
    	print("* ",* n)
    else:
    	print("*"+k*" "+"*")
    	k = k + 2
  """  	

# hollow triangle star pattern
n = 6
for i in range(1, n+1):
    for j in range(i):
        # print star only at start and end of the row
        if j == 0 or j == i-1:
            print('*', end='')
        # print only star if it's last row
        else:
            if i != n:
                print(' ', end='')
            else:
                print('*', end='')
    print()







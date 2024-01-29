"""		  1
		  0 0
		  3 3 3
		  0 0 0 0
		  5 5 5 5 5
"""		  
n = int(input("Enter the number:"))
i = 1
while i <= n:
    j = 1
    while j <= i:
        if i % 2 == 0:
            print("0", end='')
        else:
            print(i, end='')
        j = j + 1
    print()  
    i = i + 1
	

"""		5
		0 0 
		3 3 3
		0 0 0 0 
		1 1 1 1 1 

n = int(input("Enter the number: "))
i = n

while i > 0:
    j = 1
    while j <= i:
        if i % 2 == 0:
            print("0", end=" ")
        else:
            print(i, end=" ")
        j += 1
    print()
    i -= 1


		1
		2 2
		3 3 3
		4 4 4 4

n = int(input("Enter the  number:"))
i = 1
while i <= n:
    j = 1
    while j <= i:
    	print("i",end='')
	j = j + 1
    print()
    i = i - 1
   


	       1
	       3 3 
	       5 5 5
	       7 7 7 7
	       
	
n = int(input())
k = 1
for i in range(1, n + 1):
    for j in range(i):
        print(k, end='')
    print()  
    k = k + 2


			1
			1 2
			1 2 3
			1 2 3 4
		
n = int(input())
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end='')
	print()
	
    	
   			0
   			1 2
   			3 4 5
   			6 7 8 9

n = int(input("enter the number:-"))
k = 0
for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(k, end='')
		k = k + 1
	print()
 	
  	
  			0
  			0 1
  			0 1 2
  			0 1 2 3
  			0 1 2 3 4
			
n = int(input("Enter the number: "))
for i in range(0, n + 1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print()

			
			5
			5 5
			5 5 5
			5 5 5 5
		
n = int(input("Enter the number: "))
k = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(k, end=' ')
    print()


			1
			2 1
			3 2 1
			4 3 2 1

n = int(input("Enter the number: "))
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()



			1
			2 4 
			3 6 9
			4 8 12 16


n = int(input("Enter the number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j*i, end=' ')
    print()


			1
			2 3
			3 4 5
			4 5 6 7
			5 6 7 8 6

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i + j, end=' ')
    print()


			1
			1 2 1
			1 2 3 2 1
			1 2 3 4 3 2 1
			1  2 3 4 5 4 2 1
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')

    for j in range(i - 1, 0, -1):
        print(j, end='')

    print()



			0
			1 0 1
			2 1 0 1 2
			3 2 1 0 1 2 3
			4 3 2 1 0 1 2 3 4

n = int(input("Enter the number: "))
for i in range(n + 1):
 
    for j in range(i, 0, -1):
        print(j, end=' ')
    
    for j in range(i + 1):
        print(j, end=' ')
    
    print()

			
			577
			530 485
			442 401 362
			325 290 257 226
			197 170 145 122 101

n = int(input())
k = 577
p = 47
for i in range(1,n+1):
	for j in range(1,i+1):
		print(k,end=' ')
		k = k - p
		p = p - 2
	print()


			     1
			   1   2
			 1   2   3
		       1   2   3   4
		         1   2   3 
		           1   2 
		             1 
		             		       			 
n = int(input("Enter the number: "))
for i in range(1, n + 1):
  
    for j in range(n, i, -1):
        print(" ", end=' ')

    for j in range(1, i + 1):
        if j == i:
            print(j)
        else:
            print(j, end='  ')
"""










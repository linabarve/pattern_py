		
		# Fibonacci Series.........	
n=int(input())
i=1
a=0
b=1
c=a+b
while i<=n:
	if i==1:
		print(a)
		i=i+1
	else:
		print(c)
		c=a+b
		a=b
		b=c
		i=i+1




			* * * * * 
    		       * * * * * 
                     * * * * * 
  		    * * * * * 
                  * * * * * 
                  * * * * * 
                   * * * * * 
   		    * * * * * 
                     * * * * * 
                      * * * * * 

n = int(input())	
int(input())
i=1
while i<=n:
	print((n-i)*' ',end=' ')
	j=1
	while j<=n:
		print('*',end=' ')
		j=j+1
	print( )
	i=i+1
else:
	i=n-1
	k=0
	while i>=0:
		print(k*' ',end=' ')
		j=1
		while j<=n:
			print('*',end=' ')
			j=j+1
		print( )
		k=k+1
		i=i-1




			 1 
    			1 2 
 		       1 2 3 
 		      1 2 3 4 
 		     1 2 3 4 5 
  		      1 2 3 4 
   		       1 2 3 
                        1 2 
     			 1 

n = int(input())
i=1
while i<=n:
	print((n-i)*' ',end=' ')
	j=1
	while j<=i:
		print(j,end=' ')
		j=j+1
	print()
	i=i+1
i=n-1
while i>0:
 	print((n-i)*' ',end=' ')
 	j=1
 	while j<=i:
	 	print(j,end=' ')
	 	j=j+1
 	print()
 	i=i-1
"""	

  
 		# All star pattern...............
 		        *
		       * *
		      * * *
		     * * * *
		     * * * *
		      * * *
		       * *
		        *

n = int(input())
i = 1;
while i <= n:
	print((n-i) * ' ',end=' ')
	j = 1
	while j <= i:
		print('*',end=' ')
		j = j + 1
	print()
	i = i + 1
else:
	i = n
	while i > 0:
		print((n - i) * ' ',end=' ')
		j = 1
		while j <= i:
			print('* ',end='')
			j = j + 1;
		print()
		i = i - 1



		    *
		   * *
		  * * *
		 * * * *
		  * * *
		   * *
		    *
	  		        
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '* ' * i)
    
  

    
   			* * * * *
   			* * * *
   			* * *
   			* *
   			*
   			*
   			* * 
   			* * *
   			* * * *
   			* * * * *   		
n=int(input())
i=n
while i>0:
	j=1
	while j<=i:
		print('* ',end=' ')
		j=j+1
	print( )
	i=i-1
else:
	i=1
	while i<=n:
		j=1
		while j<=i:
			print('* ',end=' ')
			j=j+1
		print( )
		i=i+1




			*
			* *
			* * *
			* * * *
			* * * * *
			* * * * *
			* * * * 
			* * *
			* *
			*			
n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
		print('*',end=' ')
		j=j+1
	print()
	i=i+1
else:
	i=1
	while n>=i:
		j=1
		while j<=n:
			print('*',end=' ')
			j=j+1
		print()
		n=n-1
	



				*
			  *	*
		   	* * *
		  * * * *
		* * * * *
		* * * * *
		  * * * *
		    * * *
		      * *
		        *	
	
n=int(input())
i=1
while i<=n:
	print((n-i)*'  ',end=' ')
	j=1
	while j<=i:
		print('*',end=' ')
		j=j+1
	print()
	i=i+1
else:
	i=1
	k=0
	while n>=i:
		print(k*'  ',end=' ')
		j=1
		while j<=n:
			print('*',end=' ')
			j=j+1
		print()
		k=k+1
		n=n-1



				*
				* *
				* * *
				* * * *
				* * * * *
				* * * * 
				* * *
				* *
				*

n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
		print('*',end=' ')
		j=j+1
	print( )
	i=i+1
else:
	i=n-1
	while i>=0:
		j=1
		while j<=i:
			print('*',end=' ')
			j=j+1
		print( )
		i=i-1
	
	
	
				*
			  * *
			* * *
		  * * * *
		* * * * *
		  * * * *
		  	* * *
		  	  * *
		  	  	*	

n=int(input())
i=1
while i<=n:
	print((n-i)*'  ',end=' ')
	j=1
	while j<=i:
		print('*',end=' ')
		j=j+1
	print()
	i=i+1
i=n-1
while i>0:
	print((n-i)*'  ',end=' ')
	j=1
	while j<=i:
		print('*',end=' ')
		j=j+1
	print()
	i=i-1
	
	
	
				* * * * *
				 * * * *
				  * * *
				   * *
				    *
				    *
				   * *
				  * * *
				 * * * *
				* * * * *

n=int(input())
i=n
while i>0:
 	print((n-i)*' ',end=' ')
 	j=1
 	while j<=i:
	 	print('*',end=' ')
	 	j=j+1
 	print()
 	i=i-1
else:
 i=1
while i<=n:
	print((n-i)*' ',end=' ')
	j=1
	while j<=i:
		print('*',end=' ')
		j=j+1
	print()
	i=i+1
		        

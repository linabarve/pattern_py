"""				 * * *
				 * *
				 *
				 * 
				 * *
				 * * *

n = int(input())
for i in range(n - 1, 0, -1):
    print('* ' * i)

for i in range(1,n+1):
	print('* ' * i)
    

				*
				* *
				* * *
				* * * *
				* * * * *
				* * * *
				* * *
				* *
				*

n = int(input())
for i in range(1,n+1):
	print('* ' * i)	
for i in range(n - 1, 0, -1):
    print('* ' * i)
		   
	
				* 
			      * *
			    * * *
			  * * * *
			* * * * *
			  * * * *
			    * * *
			      * *
			        *
			        

n = int(input("Enter the number:"))
for i in range(1, n + 1):
	print((n-i) * ' ' + "*" * i)
for j in range(j, -1):
	print((n-j)*' ',+ i * '*')
	
	
	
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
			  
			  
			  
n = int(input("Enter the number:"))
for i in range(n ,0, -1):
	print((n-i) * ' ' + i * "*")
for i in range(1 ,n+1):
	print((n-i) * ' ' + i * "*")
					  
			  


			* * * *
		       	 * * *
		       	  * *
		       	   *
		       	   *
		       	  * *
		       	 * * *
		       	*  * * *	      
n = int(input())
i = n
while i > 0:
	print((n-i) * ' ',end=' ')
	j = 1
	while j <= i:
		print('*',end=' ')
		j = j + 1
	print()
	i = i - 1
else:
	i = 1
	while i <= n:
		print((n-i)*' ',end='')
		j = 1
		while j <= i:
			print('* ',end='')
			j = j + 1
		print()
		i = i + 1    


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
"""		    		        
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '* ' * i)
			  
			  
			  
			  
			  
			  
			  			

n=int(input())
i=1
k=0
while i<=n:
	while i<=2:
		print('* '*i)
		i=i+1
	while i!=n:
		print('* ',+(k+2),' '+' ',end="")
		k=k+2
		i=i+1
	print('* '*n)
	i=i+1
"""


n = int(input())
i = 1
k = 0

while i <= n:
    while i <= 2:
        print('* ' * i)
        i = i + 1
    
    while i != n:
        print('* ', (k + 2), ' ', end='')
        k = k + 2
        i = i + 1
    
    print('* ' * n)
    i = i + 1
"""
"""
i=1
k=0
while i<=n:
	while i<=2:
		print((n-i)'  ',' '*i)
		i=i+1
	while i!=n:
		print((n-i)'  ',' '+(k+2)' '+' ',end="")
		k=k+2
		i=i+1
	print((n-i)'  ',' '*n)
	i=i+1
	
n=int(input())
i=1
k=0
while i<=n:
	while i<=2:
		print((n-i)' ',' '*i)
		i=i+1
	while i!=n:
		print((n-i)' ',' '+(k+2)' '+' ')
		k=k+2
		i=i+1
	print((n-i)' ',' '*n)
	i=i+1
"""

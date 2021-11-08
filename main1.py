def perfect_square(n):
	for i in range(n/2):
        	if(i*i==n):
                	return True
                else:
			return False

n=int(input())
if(perfect_square(n)==True):
	print("given num is a perfect square")
else:
	print("not a perfect square")
	
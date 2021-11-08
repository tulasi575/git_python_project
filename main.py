def check_palindrome(str1):
	if(str1[::-1]==str1):
        	return True
        return False
str=input()
if(check_palindrome(str)==True):
	print("given string is a palindrome")
else:
	print("not a palindrome")
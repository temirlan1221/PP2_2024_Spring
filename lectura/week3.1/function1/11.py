def palindrome(text):
	size = len(text)
	for i in range(size//2):
		if text[i] != text[size - 1 - i]:
			return False
	return True

text = str(input(":"))
result = palindrome(text)
if result:
	print("this text is a palindrome")
else:
	print("No")
def palindrome(x,y):
    if x==y:
        return True
    else:
        return False
n=eval(input('enter the number:'))
binary=bin(n)
print(binary)
binary1=binary[2:]
print(binary1)
b=binary1[::-1]
print(b)
y=palindrome(b,binary1)
print(y)

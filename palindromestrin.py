n=(input("Enter the string :"))
str=n
strlen=len(n)
res=str[strlen::-1]
#print(res)
if n==res:
    print("The String is palindrome")
else:
    print("The String is not a palindrome")

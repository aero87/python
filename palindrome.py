# Python program to check if a string is a palindrome

def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

word = input("Insert a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
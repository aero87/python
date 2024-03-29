# Program to reverse a string

def reverse_string(string):
    return string[::-1]

text = input("Insert text: ")
reversed_text = reverse_string(text)
print(reversed_text)
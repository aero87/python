# Python program to find lasgest element in a list

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = list(map(int, input("Insert a series of numbers separated by a space: ").split()))

largest_num = find_largest(nums)
if largest_num is not None:
    print(f"The largest number is {largest_num}")
    
else:
    print("The list is empty.")
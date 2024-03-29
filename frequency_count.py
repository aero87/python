# Python program to count frequency of each element in a list

def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
            
        else:
            frequency[num] = 1
            
    return frequency

nums = list(map(int, input("Insert a series of numbers separated by a space: ").split()))

frequency_count = count_frequency(nums)

print(frequency_count)
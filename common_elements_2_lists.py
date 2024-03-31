# Python program to find common elements between two lists

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

list_a = list(map(int, input("Insert a series of numbers separated by a space: ").split()))
list_b = list(map(int, input("Insert a series of numbers separated by a space: ").split()))
common = find_common_elements(list_a, list_b)

print(common)
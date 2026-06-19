def swap_elements(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

swap_elements(numbers, i, j)

print("Updated List:", numbers)

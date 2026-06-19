numbers = [12, 45, 7, 89, 23, 56, 34, 90, 11, 67]

print("List:", numbers)

# Maximum, Minimum, Average
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

# Sorting
print("Ascending Order:", sorted(numbers))
print("Descending Order:", sorted(numbers, reverse=True))

# Add a new number
new_num = int(input("Enter a new number: "))
numbers.append(new_num)

# Remove first item
numbers.pop(0)

print("Updated List:", numbers)

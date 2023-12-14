# Create a sample list
my_list = [10, 20, 30, 40, 50]

# Print the original list
print("Original list:", my_list)

# Prompt the user for the old number and the new number
old_number = int(input("Enter the old number: "))
new_number = int(input("Enter the new number: "))

# Check if the old number exists in the list and replace it
if old_number in my_list:
    index = my_list.index(old_number)  # Find the index of the old number
    my_list.remove(old_number)         # Remove the old number
    my_list.insert(index, new_number)  # Insert the new number at the same index
else:
    print(f"{old_number} is not in the list.")

# Print the modified list
print("Modified list:", my_list)

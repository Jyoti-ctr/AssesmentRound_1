def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Checking if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# user input
input_string = input("Enter a string to check if it's a palindrome: ")
# Check if the input string is a palindrome and print the result
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:

    print(f'"{input_string}" is not a palindrome.')

counter = 0
for i in range(0, len(input_string)-1+1, 1):
    for j in range(i+1, len(input_string)-1+1, 1):
        if input_string[i] == input_string[j]:
            counter += 1
print(f'Number of duplicate characters in the input string: {counter}')
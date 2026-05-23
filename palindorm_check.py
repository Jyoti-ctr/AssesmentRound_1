def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Get user input
input_string = input("Enter a string to check if it's a palindrome: ")
# Check if the input string is a palindrome and print the result
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:

    print(f'"{input_string}" is not a palindrome.')